import pygame


def create_board(surf, width, height, border_width, color, line_width):
    pygame.draw.polygon(surf, color, [[0, 0], [border_width, border_width],
                                      [border_width, height - border_width],
                                      [0, height]], width=line_width)
    pygame.draw.polygon(surf, color, [[0, 0], [border_width, border_width],
                                      [width - border_width, border_width],
                                      [width, 0]], width=line_width)
    pygame.draw.polygon(surf, color, [[width, height], [width - border_width,
                                                        height - border_width],
                                      [width - border_width, border_width],
                                      [width, 0]], width=line_width)
    pygame.draw.polygon(surf, color, [[width, height], [width - border_width,
                                                        height - border_width],
                                      [border_width, height - border_width],
                                      [0, height]], width=line_width)
    line_width = 1 if line_width == 0 else line_width
    pygame.draw.polygon(surf, (0, 0, 0),
                        [[0, 0], [width - line_width, 0],
                         [width - line_width, height - line_width],
                         [0, height - line_width]], width=line_width)
