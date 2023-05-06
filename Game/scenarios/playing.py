from Game.game_setup.game_create import get_screen, get_clock
from Game.game_setup.colors import GREEN, BLACK
from Game.game_setup.get_info import get_playing_button_mask
from Game.help_func.word_draw import playing_word_surf
from Game.graphic_elements.background import create_background
from Game.graphic_elements.button import Static_button
from Game.graphic_elements.logo import create_logo
from Game.states.game_states import Button_type, Button_data, Event_type, Game_scenarios, Game_result
from Game.game_setup.config_reader import fps
from Game.scenarios.get_event import event

from Game.help_func.error_draw import error_upper_right_corner, get_error_text, error_bottom_left_corner
import pygame as pg


def play():
    game_loop(word_true='АДАТАР')
    return Game_scenarios.main_menu


def create_screen_detail():
    surf = create_background()
    logo, logo_coord = create_logo()
    surf.blit(logo, logo_coord)

    buttons = []

    button_texts = ['Главное меню']
    button_states = [Button_data.return_menu]
    button_masks = get_playing_button_mask()
    buttons_types = [Button_type.Scenario]

    for mask, text, callback_data, button_type in zip(button_masks, button_texts, button_states, buttons_types):
        buttons.append(Static_button(width=mask["size"][0], height=mask["size"][1],
                                     text=text, coords=mask["coord"], callback_data=callback_data,
                                     type=button_type))

    return surf, buttons


def game_loop(word_true: str):
    screen = get_screen()
    clock = get_clock()

    health = 5

    surf, buttons = create_screen_detail()
    screen.blit(surf, (0, 0))

    word_dict = word_parse(word_text=word_true)
    current_word = '*' * len(word_true)
    log = []

    message_yes = get_error_text("Вы отгадали\n букву", color=GREEN, prescription=False)
    message_no = get_error_text("Вы не отгадали букву", prescription=False)
    error_repeat = get_error_text("Вы уже пробовали эту букву", prescription=False)
    current_message = None


    running = True
    while True:
        clock.tick(fps)
        screen.blit(surf, (0, 0))

        playing_word_surf(screen, current_word)
        log_text = get_error_text(f'Log: {", ".join(log)}', color=BLACK, prescription=False)
        error_bottom_left_corner(screen, log_text)

        if current_message:
            error_upper_right_corner(screen, current_message)

        if health == 0:
            return Game_scenarios.main_menu, Game_result.Lose

        if not current_word.count('*'):
            return Game_scenarios.main_menu, Game_result.Win

        event_type, event_data = event(surf=screen, buttons=buttons, text_input=True)

        if event_type == Event_type.Quit:
            return Game_scenarios.exit_game, Game_result.Lose
        if event_type == Button_type.Scenario:
            if event_data == Button_data.return_menu:
                return Game_scenarios.main_menu, Game_result.Lose
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