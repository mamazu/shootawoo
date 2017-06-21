from Camera import Renderable
from pygame.draw import circle
from VecMath import Vec2D

class Ball(Renderable):
    def __init__(self):
        self.pos = Vec2D(200, 10)
        self.acc = Vec2D(.2, .5)
        self.speed = Vec2D()

    def update(self):
        self.pos += self.speed
        self.speed += self.acc

    def show(self, screen):
        circle(screen, (255, 0, 0), self.pos.getTuple(), 30)
