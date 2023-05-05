import pygame as pg
from Game.game_setup.get_info import get_logo_info


def create_logo():
    logo_info = get_logo_info()
    logo = pg.image.load('Game/templates/logo.jpg')
    logo.set_colorkey((255, 255, 255))

    logo = pg.transform.scale(logo, logo_info['size'])

    return logo, logo_info['coord']
