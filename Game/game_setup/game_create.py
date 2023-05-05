import pygame as pg


def start_game():
    global screen, clock
    pg.init()
    pg.mixer.init()
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    pg.display.set_caption("Gallow game")
    clock = pg.time.Clock()


def get_screen():
    return screen


def get_clock():
    return clock


def get_middle():
    return screen.get_size()


def close_game():
    pg.quit()