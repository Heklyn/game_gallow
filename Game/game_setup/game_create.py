import pygame as pg
from Game.db.sqlite import db_start


def start_game():
    global screen, clock
    pg.init()
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    pg.display.set_caption("Gallow game")
    clock = pg.time.Clock()
    db_start()


def get_screen():
    return screen


def get_clock():
    return clock


def close_game():
    pg.quit()
