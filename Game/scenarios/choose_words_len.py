from Game.game_setup.game_create import get_screen, get_clock
from Game.game_setup.get_info import get_choose_word_len_button_mask
from Game.graphic_elements.word_draw import word_center
from Game.graphic_elements.background import create_background
from Game.graphic_elements.button import Static_button
from Game.states.game_states import Button_type, Button_data, Event_type, Game_scenarios
from Game.game_setup.config_reader import fps
from Game.scenarios.get_event import game_event
from Game.game_setup.config_reader import max_word_len, min_word_len
from Game.graphic_elements.error_draw import error_upper_right_corner, get_error_text
import pygame as pg


def play():
    new_game_state, word_len = game_loop()
    return new_game_state, word_len


def create_screen_detail():
    surf = create_background()

    buttons = []

    button_texts = ['Играть', 'Отнять', 'Прибавить', 'Главное меню']
    button_states = [Button_data.accept, Button_data.length_minus,
                     Button_data.length_plus, Button_data.return_menu]
    button_masks = get_choose_word_len_button_mask()
    buttons_types = [Button_type.Scenario, Button_type.Playing, Button_type.Playing, Button_type.Scenario]

    for mask, text, callback_data, button_type in zip(button_masks, button_texts, button_states, buttons_types):
        buttons.append(Static_button(width=mask["size"][0], height=mask["size"][1],
                                     text=text, coords=mask["coord"], callback_data=callback_data,
                                     button_type=button_type))

    return surf, buttons


def game_loop():
    screen = get_screen()
    clock = get_clock()

    surf, buttons = create_screen_detail()
    screen.blit(surf, (0, 0))

    error_no_more = get_error_text("Достигнута максимальная длина")
    error_no_less = get_error_text("Достигнута минимальная длина")

    word_len = min_word_len

    current_error = None

    running = True
    while True:
        clock.tick(fps)
        screen.blit(surf, (0, 0))

        if current_error:
            error_upper_right_corner(screen, current_error)

        word_center(screen, f"Длина слова: {word_len}")

        event_type, event_data = game_event(surf=screen, buttons=buttons)

        if event_type == Event_type.Quit:
            return Game_scenarios.exit_game, None
        if event_type == Button_type.Scenario:
            if event_data == Button_data.return_menu:
                return Game_scenarios.main_menu, None
            if event_data == Button_data.accept:
                return Game_scenarios.playing, word_len
        if event_type == Button_type.Playing:
            if event_data == Button_data.length_plus:
                if word_len == max_word_len:
                    current_error = error_no_more
                else:
                    word_len += 1
                    current_error = None
            if event_data == Button_data.length_minus:
                if word_len == min_word_len:
                    current_error = error_no_less
                else:
                    word_len -= 1
                    current_error = None

        pg.display.flip()
