from Game.game_setup.game_create import get_screen, get_clock
from Game.game_setup.colors import GREEN, BLACK, win_color, lose_color
from Game.game_setup.get_info import get_playing_button_mask
from Game.graphic_elements.word_draw import playing_word_surf
from Game.graphic_elements.background import create_background
from Game.graphic_elements.button import Static_button
from Game.states.game_states import Button_type, Button_data, Event_type, Game_scenarios, Game_result, Allow_input
from Game.game_setup.config_reader import fps, update_score
from Game.scenarios.get_event import game_event
from Game.graphic_elements.gallow import Gallow
from Game.game_setup.get_info import get_playing_gallow_mask


from Game.graphic_elements.error_draw import error_upper_right_corner, get_error_text, error_bottom_left_corner
import pygame as pg


def play(word: str):
    new_game_state, game_result = game_loop(word_true=word)
    if game_result == Game_result.Win:
        update_score(is_win=True)
    elif game_result == Game_result.Lose:
        update_score(is_win=False)

    return new_game_state


def create_screen_detail():
    surf = create_background()

    buttons = []

    button_texts = ['Главное меню']
    button_states = [Button_data.return_menu]
    button_masks = get_playing_button_mask()
    buttons_types = [Button_type.Scenario]

    for mask, text, callback_data, button_type in zip(button_masks, button_texts, button_states, buttons_types):
        buttons.append(Static_button(width=mask["size"][0], height=mask["size"][1],
                                     text=text, coords=mask["coord"], callback_data=callback_data,
                                     button_type=button_type))

    return surf, buttons


def game_loop(word_true: str):
    screen = get_screen()
    clock = get_clock()

    health = 6

    surf, buttons = create_screen_detail()
    screen.blit(surf, (0, 0))

    gallow_info = get_playing_gallow_mask()
    gallow = Gallow(screen=screen, pos=gallow_info["pos"], scale=gallow_info["scale"])

    word_dict = word_parse(word_text=word_true)
    current_word = '*' * len(word_true)
    log = []

    message_yes = get_error_text("Вы отгадали букву", color=GREEN, prescription=False)
    message_no = get_error_text("Вы не отгадали букву", prescription=False)
    error_repeat = get_error_text("Вы уже пробовали эту букву", prescription=False)
    message_win = get_error_text(f"Вы выиграли, слово: {word_true}", color=GREEN, prescription=False)
    message_lose = get_error_text(f"Вы проиграли, слово: {word_true}", prescription=False)
    current_message = None

    game_result = Game_result.Lose
    is_allow_input = Allow_input.Yes

    running = True
    while True:
        clock.tick(fps)
        screen.blit(surf, (0, 0))

        gallow.draw()

        playing_word_surf(screen, current_word)
        log_text = get_error_text(f'Log: {", ".join(log)}', color=BLACK, prescription=False)
        error_bottom_left_corner(screen, log_text)

        if current_message:
            error_upper_right_corner(screen, current_message)

        event_type, event_data = game_event(surf=screen, buttons=buttons, text_input=is_allow_input)

        if event_type == Event_type.Quit:
            return Game_scenarios.exit_game, game_result
        if event_type == Button_type.Scenario:
            if event_data == Button_data.return_menu:
                return Game_scenarios.main_menu, game_result
        if event_type == Event_type.Key_press:
            if event_data in log:
                current_message = error_repeat
            else:
                if event_data != 'backspace':
                    if event_data in word_dict.keys():
                        word_list = list(current_word)
                        for index in word_dict[event_data]:
                            word_list[index] = event_data
                        current_word = ''.join(word_list)
                        current_message = message_yes
                    else:
                        current_message = message_no
                        health -= 1
                        gallow.next_state()

                    if health == 0:
                        is_allow_input = Allow_input.No
                        surf = create_background(current_color=lose_color)
                        current_message = message_lose

                    if not current_word.count('*'):
                        game_result = Game_result.Win
                        is_allow_input = Allow_input.No
                        surf = create_background(current_color=win_color)
                        current_message = message_win

                    log.append(event_data)

        pg.display.flip()


def word_parse(word_text: str):
    word_dict = {}
    for i, letter in enumerate(word_text):
        if letter in word_dict.keys():
            word_dict[letter].append(i)
        else:
            word_dict[letter] = [i, ]

    return word_dict
