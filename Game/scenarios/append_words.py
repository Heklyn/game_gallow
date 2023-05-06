from Game.game_setup.game_create import get_screen, get_clock
from Game.game_setup.get_info import get_append_words_button_mask
from Game.db import sqlite
from Game.help_func.word_draw import word_center
from Game.graphic_elements.background import create_background
from Game.graphic_elements.button import Static_button
from Game.graphic_elements.logo import create_logo
from Game.states.game_states import Button_type, Button_data, Event_type, Game_scenarios, File_code, Word_code
from Game.game_setup.config_reader import fps
from Game.scenarios.get_event import event
from Game.help_func.file_reader import Txt_reader
from Game.help_func.error_draw import error_bottom_right_corner, get_error_text
import pygame as pg


def play():
    return game_loop(), None


def create_screen_detail():
    surf = create_background()
    logo, logo_coord = create_logo()
    surf.blit(logo, logo_coord)

    file = Txt_reader(file_name='words.txt')
    status = file.open_file()

    buttons = []

    button_texts = ['Не подходит', 'Подходит', 'Главное меню']
    button_states = [Button_data.skip, Button_data.accept, Button_data.return_menu]
    button_masks = get_append_words_button_mask()
    buttons_types = [Button_type.Playing, Button_type.Playing, Button_type.Scenario]

    for mask, text, callback_data, button_type in zip(button_masks, button_texts, button_states, buttons_types):
        buttons.append(Static_button(width=mask["size"][0], height=mask["size"][1],
                                     text=text, coords=mask["coord"], callback_data=callback_data,
                                     type=button_type))
    text_error = None
    if status == File_code.Not_exist:
        text_error = get_error_text(text='Файл со словами не найден')
        buttons[0].disable()
        buttons[1].disable()

    return surf, buttons, text_error, file


def game_loop():
    screen = get_screen()
    clock = get_clock()

    surf, buttons, error_text, file = create_screen_detail()
    screen.blit(surf, (0, 0))

    if error_text:
        error_bottom_right_corner(surf, error_text)

    error_text = get_error_text("В файле закончились слова")
    flag_next = True
    current_word = ''

    running = True
    while True:
        clock.tick(fps)
        screen.blit(surf, (0, 0))

        if flag_next:
            status, word = file.get_word()
            if status == Word_code.Not_get:
                buttons[0].disable()
                buttons[1].disable()
                error_bottom_right_corner(surf, error_text)
            else:
                current_word = word.upper()
            flag_next = False

        word_center(screen, current_word)

        event_type, event_data = event(surf=screen, buttons=buttons)

        if event_type == Event_type.Quit:
            return Game_scenarios.exit_game
        if event_type == Button_type.Scenario:
            if event_data == Button_data.return_menu:
                return Game_scenarios.main_menu
        if event_type == Button_type.Playing:
            if event_data == Button_data.accept:
                sqlite.create_word(word=current_word)
            flag_next = True

        pg.display.flip()


