from Game.game_setup.config_reader import get_stats, gap
from Game.graphic_elements.word_draw import surf_text
from Game.game_setup.game_create import get_screen
import pygame as pg


def add_stats(surface: pg.Surface):
    size_screen = get_screen().get_size()
    game, win, lose = get_stats()

    text_surfs = [
        surf_text(f"Всего игр: {game}"),
        surf_text(f"Побед: {win}"),
        surf_text(f"Поражений: {lose}"),
    ]

    max_height = max([surf.get_size()[1] for surf in text_surfs])

    start_height = size_screen[1] - max_height * 3 - gap * size_screen[0] * 4

    for i, surf in enumerate(text_surfs):
        surface.blit(surf, (gap * size_screen[0] * 2, start_height + i * max_height + gap * size_screen[0] * i))
