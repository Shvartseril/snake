from pygame import Surface, draw, display

from utils.colors import RED


class Field:
    def __init__(self, screen: Surface):
        self.screen = screen
        print(screen)

    def draw_field(self):
        draw.line(self.screen, RED, (0, 0), (100, 100), 20)
        display.flip()
