from Game.graphic_elements.stats import add_stats
from Game.game_setup.game_create import get_screen, get_clock
from Game.game_setup.config_reader import fps
from Game.graphic_elements.button import Static_button
from Game.game_setup.get_info import get_main_menu_button_masks, get_main_menu_gallow_mask
from Game.graphic_elements.background import create_background
from Game.states.game_states import Button_data, Button_type, Game_scenarios, Event_type, Playing_type
from Game.scenarios.get_event import event
from Game.graphic_elements.gallow import Gallow
from Game.graphic_elements.error_draw import get_error_text, error_upper_right_corner
import pygame as pg


def create_screen_detail(current_error):
    surf = create_background()

    add_stats(surf)

    for gallow_info in get_main_menu_gallow_mask():
        gallow = Gallow(screen=surf, pos=gallow_info["pos"], scale=gallow_info["scale"])
        gallow.max_state()
        gallow.draw()

    buttons = []

    button_texts = ['Быстрая игра', 'Определенная длина', 'Задать слово', 'Добавить в бд', "Выход"]
    button_states = [Button_data.fast_play, Button_data.play_with_fixed_length,
                     Button_data.play_with_given_word, Button_data.add_word_to_db,
                     Button_data.exit_game]
    button_masks = get_main_menu_button_masks()

    for mask, text, callback_data in zip(button_masks, button_texts, button_states):
        buttons.append(Static_button(width=mask["size"][0], height=mask["size"][1],
                                     text=text, coords=mask["coord"], callback_data=callback_data,
                                     button_type=Button_type.Scenario))

    if current_error:
        message_error = get_error_text(current_error)
        error_upper_right_corner(screen=surf, error_text=message_error)

    return surf, buttons


def play(current_error):
    new_game_state = game_loop(current_error)
    if new_game_state == Game_scenarios.playing:
        return Game_scenarios.playing, Playing_type.fast_play
    return new_game_state, None


def game_loop(current_error):
    screen = get_screen()
    clock = get_clock()

    surf, buttons = create_screen_detail(current_error)

    running = True
    while running:
        clock.tick(fps)
        screen.blit(surf, (0, 0))

        event_type, event_data = event(surf=screen, buttons=buttons)
        if event_type == Event_type.Quit:
            return Game_scenarios.exit_game
        if event_type == Button_type.Scenario:
            if event_data == Button_data.fast_play:
                new_game_state = Game_scenarios.playing
            elif event_data == Button_data.play_with_fixed_length:
                new_game_state = Game_scenarios.choose_words_len
            elif event_data == Button_data.play_with_given_word:
                new_game_state = Game_scenarios.enter_word
            elif event_data == Button_data.exit_game:
                new_game_state = Game_scenarios.exit_game
            elif event_data == Button_data.add_word_to_db:
                new_game_state = Game_scenarios.append_words
            else:
                raise Exception('Wrong button_callback_data')
            return new_game_state

        pg.display.flip()
