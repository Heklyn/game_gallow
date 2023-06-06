from Game.game_setup.game_create import get_screen, get_clock
from Game.game_setup.get_info import get_enter_word_button_mask
from Game.graphic_elements.word_draw import word_center
from Game.graphic_elements.background import create_background
from Game.graphic_elements.button import Static_button
from Game.states.game_states import Button_type, Button_data, Event_type, Game_scenarios, Allow_input
from Game.game_setup.config_reader import fps
from Game.scenarios.get_event import game_event
from Game.game_setup.config_reader import max_word_len, min_word_len
from Game.graphic_elements.error_draw import error_upper_right_corner, get_error_text
from Game.db.sqlite import is_word_in_db, create_word
import pygame as pg


def play():
    new_game_state, word = game_loop()
    if word:
        if not is_word_in_db(word=word):
            create_word(word=word)
    return new_game_state, word


def create_screen_detail():
    surf = create_background()

    buttons = []

    button_texts = ['Играть', 'Главное меню']
    button_states = [Button_data.accept, Button_data.return_menu]
    button_masks = get_enter_word_button_mask()
    buttons_types = [Button_type.Scenario, Button_type.Scenario]

    for mask, text, callback_data, button_type in zip(button_masks, button_texts, button_states, buttons_types):
        buttons.append(Static_button(width=mask["size"][0], height=mask["size"][1],
                                     text=text, coords=mask["coord"], callback_data=callback_data,
                                     button_type=button_type))
    buttons[0].disable()

    return surf, buttons


def game_loop():
    screen = get_screen()
    clock = get_clock()

    surf, buttons = create_screen_detail()
    screen.blit(surf, (0, 0))

    error_no_more = get_error_text("Слово слишком длинное")
    error_no_less = get_error_text("Слово слишком короткое")

    word = ''

    current_error = error_no_less

    running = True
    while True:
        clock.tick(fps)
        screen.blit(surf, (0, 0))

        if current_error:
            error_upper_right_corner(screen, current_error)

        word_center(screen, f"Ваше слово: {word}")

        event_type, event_data = game_event(surf=screen, buttons=buttons, text_input=Allow_input.Yes)

        if event_type == Event_type.Quit:
            return Game_scenarios.exit_game, None

        if event_type == Button_type.Scenario:
            if event_data == Button_data.return_menu:
                return Game_scenarios.main_menu, None
            if event_data == Button_data.accept:
                return Game_scenarios.playing, word

        if event_type == Event_type.Key_press:

            if event_data == 'backspace':
                if len(word) > 0:
                    word = word[:-1]
            else:
                if len(word) < max_word_len + 5:
                    word += event_data

            if len(word) < min_word_len:
                current_error = error_no_less
                buttons[0].disable()
            elif len(word) > max_word_len:
                current_error = error_no_more
                buttons[0].disable()
            else:
                current_error = None
                buttons[0].enable()

        pg.display.flip()
