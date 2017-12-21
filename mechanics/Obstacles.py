from tools.VecMath import Vec2D

from pygame.draw import rect

from Camera import Renderable


class Platform(Renderable):
    def __init__(self):
        self.position = Vec2D(0, 400)

    def show(self, screen, offset):
        pos_x, pos_y = (self.position - offset).get_tuple()
        rect(screen, (0, 0, 0), (pos_x, pos_y, 100, 300))
