from Game.game_setup.get_info import get_background_info
from Game.game_setup.game_create import get_screen
from Game.game_setup.colors import line_color, list_color, red_line_color
import pygame as pg


def create_background():
    size = get_screen().get_size()
    background_surf = pg.Surface(size=size)

    background_surf.fill(list_color)

    background_info = get_background_info()

    for x_line in range(1, background_info['num_x'] + 1):
        pg.draw.line(background_surf, color=line_color,
                     start_pos=(x_line * background_info['side_len'], 0),
                     end_pos=(x_line * background_info['side_len'], size[1]),
                     width=2)

    for y_line in range(1, background_info['num_x'] + 1):
        pg.draw.line(background_surf, color=line_color,
                     start_pos=(0, y_line * background_info['side_len']),
                     end_pos=(size[0], y_line * background_info['side_len']),
                     width=2)

    pg.draw.line(background_surf, color=red_line_color,
                 start_pos=(round(background_info['side_len'] * 2.5), 0),
                 end_pos=(round(background_info['side_len'] * 2.5), size[1]),
                 width=3)

    return background_surf
