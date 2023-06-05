import pygame as pg
from Game.game_setup.colors import GREY_Gainsboro, GREY, GREY_Dark, BLACK
from Game.graphic_elements.border import create_board
from Game.states.game_states import Button_type


class Static_button:
    def __init__(self, width: int, height: int, text: str, coords: tuple, callback_data, font_size: int = 40,
                 font_color: tuple = BLACK, border_width: int = -1, border_width_hover_coef: float = 0.5,
                 border_color: tuple = BLACK, line_width: int = 1, color_normal: tuple = GREY_Gainsboro,
                 color_hover: tuple = GREY_Dark, color_off: tuple = GREY, button_type: Button_type = None):
        self.width = width
        self.height = height
        self.text = text
        self.coords = coords
        self.callback_data = callback_data
        self.font_size = font_size
        self.font_color = font_color
        if border_width + 1:
            self.border_width = border_width
        else:
            self.border_width = round(min(self.width, self.height) * 0.1)
        self.border_width_hover_coef = border_width_hover_coef
        self.border_width_hover = round(self.border_width * self.border_width_hover_coef)
        self.line_width = line_width
        self.color_normal = color_normal
        self.color_hover = color_hover
        self.color_off = color_off
        self.enabled = True
        self.rect = [[coords[0], coords[0] + width], [coords[1], coords[1] + height]]
        self.border_color = border_color
        self.button_type = button_type

        self.surf1 = self.create_surf(border_width=self.border_width, color=self.color_normal)
        self.surf2 = self.create_surf(border_width=self.border_width_hover, color=self.color_hover)
        self.surf3 = self.create_surf(border_width=self.border_width, color=self.color_off)

    def draw(self, screen, mouse_pos):
        if self.enabled:
            if self.collidepoint(mouse_pos):
                screen.blit(self.surf2, self.coords)
            else:
                screen.blit(self.surf1, self.coords)
        else:
            screen.blit(self.surf3, self.coords)

    def create_surf(self, border_width, color):
        surf = pg.Surface((self.width, self.height))
        surf.fill(color)
        create_board(surf, width=self.width, height=self.height, border_width=border_width,
                     color=self.border_color, line_width=1)
        font = pg.font.Font(None, self.font_size)
        text = font.render(self.text, True,
                           self.font_color)
        surf.blit(text, [(self.width - text.get_size()[0]) / 2, (self.height - text.get_size()[1]) / 2])
        return surf

    def collidepoint(self, pos):
        if self.rect[0][0] <= pos[0] <= self.rect[0][1] and self.rect[1][0] <= pos[1] <= self.rect[1][1]:
            return True
        return False

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def is_pressed(self, pos):
        if self.enabled and self.collidepoint(pos):
            return self.callback_data
        return None

    def disable_with_color(self, color):
        self.enabled = False
        self.surf3 = self.create_surf(border_width=self.border_width, color=color)
