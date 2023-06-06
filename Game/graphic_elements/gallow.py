import pygame as pg

from Game.game_setup.game_create import get_screen
from Game.game_setup.colors import tree_color, body_color, rope_color

construction_info = {
    "max_state": 0,
    "width_scale": 0.1,
    "height_scale": 0.13,
}

gallow_info = {
    "max_state": 6,
    "width": 0.7,
    "height": 0.2,
}

man_info = {
    "max_state": 6,
    "body_dim": ((0.325, 0.35), (0.35, 0.4)),
    "head_dim": ((0.4, 0.21), (0.2, 0.15)),
    "hand_len": 0.6,
    "rope_dim": ((0.45, 0.35), (0.45, 0.55))
}


class Base_draw:
    def __init__(self, screen, pos):
        self.pos = pos
        self.state = 0
        self.screen = screen

    def reset(self):
        self.state = 0

    def next_state(self):
        self.state += 1

    def max_state(self):
        self.state = 10


class Gallow(Base_draw):
    def __init__(self, screen, pos, scale=1):
        super().__init__(screen, pos)
        height = get_screen().get_size()[1] * gallow_info["height"] * scale
        width = height * gallow_info["width"]
        self.construction = Construction(screen=screen, pos=pos, dimensions=(width, height))
        self.man = Man(screen=screen, pos=pos, dimensions=(width, height))

    def reset(self):
        super().reset()
        self.construction.reset()
        self.man.reset()

    def max_state(self):
        self.state = gallow_info["max_state"]
        self.construction.max_state()
        self.man.max_state()

    def next_state(self):
        super().next_state()
        self.man.next_state()

    def draw(self):
        self.construction.draw()
        self.man.draw()


class Construction(Base_draw):
    def __init__(self, screen, pos, dimensions):
        self.dimensions = dimensions
        super().__init__(screen, pos)

    def max_state(self):
        self.state = construction_info["max_state"]

    def draw(self):
        self.draw_part_one()
        self.draw_part_two()
        self.draw_part_three()

    def draw_part_one(self):
        pg.draw.line(self.screen, tree_color, start_pos=self.pos,
                     end_pos=(self.pos[0], self.pos[1] + self.dimensions[1]),
                     width=10)

    def draw_part_two(self):
        pg.draw.line(self.screen, tree_color, start_pos=self.pos,
                     end_pos=(self.pos[0] + self.dimensions[0], self.pos[1]),
                     width=10)

    def draw_part_three(self):
        pg.draw.line(self.screen, tree_color,
                     start_pos=(self.pos[0] + self.dimensions[0] * construction_info["width_scale"], self.pos[1]),
                     end_pos=(self.pos[0], self.pos[1] + self.dimensions[1] * construction_info["height_scale"]),
                     width=7)


class Man(Base_draw):
    def __init__(self, screen, pos, dimensions):
        super().__init__(screen, pos)
        self.dimensions = dimensions

    def max_state(self):
        self.state = man_info["max_state"]

    def draw(self):
        if self.state == 1:
            self.draw_state_one()
        elif self.state == 2:
            self.draw_state_two()
        elif self.state >= 3:
            self.draw_state_three()

    def draw_state_two(self):
        pg.draw.ellipse(self.screen, body_color,
                        (self.pos[0] + self.dimensions[0] * man_info["body_dim"][0][0],
                         self.pos[1] + self.dimensions[1] * man_info["body_dim"][0][1],
                         self.dimensions[0] * man_info["body_dim"][1][0],
                         self.dimensions[1] * man_info["body_dim"][1][1]))
        self.draw_state_one()

    def get_end_positions(self):
        positions = []
        for y_coord in [0, self.dimensions[1]]:
            for x_coord in [0, self.dimensions[0]]:
                positions.append((
                    self.pos[0] + x_coord,
                    self.pos[1] + y_coord
                ))
        return positions

    def draw_state_one(self):
        pg.draw.ellipse(self.screen, body_color,
                        (self.pos[0] + self.dimensions[0] * man_info["head_dim"][0][0],
                         self.pos[1] + self.dimensions[1] * man_info["head_dim"][0][1],
                         self.dimensions[0] * man_info["head_dim"][1][0],
                         self.dimensions[1] * man_info["head_dim"][1][1]))

        pg.draw.line(self.screen, rope_color,
                     start_pos=(self.pos[0] + man_info["rope_dim"][0][0] * self.dimensions[0], self.pos[1] - 6),
                     end_pos=(self.pos[0] + man_info["rope_dim"][0][0] * self.dimensions[0],
                              self.pos[1] + man_info["rope_dim"][0][1] * self.dimensions[1] + 2),
                     width=7)

        pg.draw.line(self.screen, rope_color,
                     start_pos=(self.pos[0] + man_info["rope_dim"][1][0] * self.dimensions[0],
                                self.pos[1] + man_info["rope_dim"][0][1] * self.dimensions[1]),
                     end_pos=(self.pos[0] + man_info["rope_dim"][1][1] * self.dimensions[0],
                              self.pos[1] + man_info["rope_dim"][0][1] * self.dimensions[1]),
                     width=6)

    def draw_state_three(self):
        self.draw_state_two()
        for i in range(self.state - 2):
            self.draw_hand(end_pos=self.get_end_positions()[i])

    def draw_hand(self, end_pos):

        middle_pos = (self.pos[0] + self.dimensions[0] / 2,
                      self.pos[1] + self.dimensions[1]
                      * (man_info["body_dim"][0][1] + man_info["body_dim"][1][1] / 2))

        pg.draw.line(self.screen, body_color, start_pos=middle_pos,
                     end_pos=(middle_pos[0] + (end_pos[0] - middle_pos[0]) * man_info["hand_len"],
                              middle_pos[1] + (end_pos[1] - middle_pos[1]) * man_info["hand_len"] * 0.9),
                     width=10)
