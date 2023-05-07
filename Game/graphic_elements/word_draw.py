import pygame as pg
from Game.game_setup.colors import BLACK
from Game.game_setup.config_reader import gap
from Game.game_setup.game_create import get_screen


def surf_text(word_text: str):
    font = pg.font.Font(None, 72)
    word = font.render(word_text, True, BLACK)
    return word


def word_center(surf: pg.surface.Surface, word_text: str):
    word = surf_text(word_text=word_text)
    surf_size = surf.get_size()
    word_size = word.get_size()

    coord = (
        (surf_size[0] - word_size[0]) // 2,
        (surf_size[1] - word_size[1]) // 2
    )

    surf.blit(word, coord)


def playing_word_surf(surface: pg.Surface, word_text: str):
    screen_size = get_screen().get_size()
    letter_surfs = [surf_text(letter) for letter in word_text]
    max_height = max([surf.get_size()[1] for surf in letter_surfs]) + 10
    all_width = sum([surf.get_size()[0] for surf in letter_surfs]) + gap * (len(word_text) - 1) * screen_size[0]

    sums_width = [0, ]
    for surf in letter_surfs[:-1]:
        sums_width.append(sums_width[-1] + surf.get_size()[0])

    coords = (
        (screen_size[0] - all_width) // 2,
        (screen_size[1] - max_height) // 2
    )

    for i, (letter_width, surf) in enumerate(zip(sums_width, letter_surfs)):
        surface.blit(surf, (coords[0] + letter_width + i * gap * screen_size[0], coords[1]))
        pg.draw.line(surface, BLACK,
                     (coords[0] + letter_width + i * gap * screen_size[0], coords[1] + max_height),
                     (coords[0] + letter_width + i * gap * screen_size[0] + surf.get_size()[0], coords[1] + max_height),
                     width=10)
