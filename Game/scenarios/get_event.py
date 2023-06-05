import pygame as pg
from Game.states.game_states import Event_type, Allow_input
from Game.help_func.key_input import get_letter


def event(surf: pg.Surface, buttons: list, text_input: Allow_input = Allow_input.No):
    mouse_pos = pg.mouse.get_pos()
    for button in buttons:
        button.draw(surf, mouse_pos)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            return Event_type.Quit, None
        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pressed()[0]:
                for button in buttons:
                    if button.is_pressed(mouse_pos):
                        return button.button_type, button.callback_data
        if text_input == Allow_input.Yes and event.type == pg.KEYDOWN:
            letter = get_letter(event.key)
            if letter:
                return Event_type.Key_press, letter

    return Event_type.Not_event, None
