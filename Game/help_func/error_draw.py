from pygame.surface import Surface
from Game.game_setup.colors import RED
import pygame as pg


def error_bottom_right_corner(screen: Surface, error_text: Surface):
    screen_size = screen.get_size()
    text_size = error_text.get_size()
    screen.blit(error_text, (screen_size[0] - text_size[0] - 20, screen_size[1] - text_size[1] - 20))


def error_bottom_left_corner(screen: Surface, error_text: Surface):
    screen_size = screen.get_size()
    text_size = error_text.get_size()
    screen.blit(error_text, (20, screen_size[1] - text_size[1] - 20))


def error_upper_right_corner(screen: Surface, error_text: Surface):
    screen_size = screen.get_size()
    text_size = error_text.get_size()
    screen.blit(error_text, (screen_size[0] - text_size[0] - 20, 20))


def get_error_text(text: str, color: tuple = RED, prescription: bool = True):
    font = pg.font.Font(None, 52)
    prescription_text = ''
    if prescription:
        prescription_text = 'Error: '
    text_error = font.render(f"{prescription_text}{text}", True, color)
    return text_error
