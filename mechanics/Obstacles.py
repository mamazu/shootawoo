from tools.VecMath import Vec2D

from pygame.draw import rect

from Camera import Renderable


class Platform(Renderable):
    def __init__(self):
        self.position = Vec2D(0, 400)

    def show(self, screen, offset):
        posX, posY = (self.position - offset).getTuple()
        rect(screen, (0, 0, 0), (posX, posY, 100, 300))
