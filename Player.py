from Camera import Renderable
from pygame.draw import circle
from VecMath import Vec2D

class Ball(Renderable):
    def __init__(self):
        self.position = Vec2D(400, 0)
        self.speed = Vec2D(0, 0)
        self.acceleration = Vec2D(0, 1)

    def update(self):
        self.position += self.speed
        self.speed += self.acceleration

    def show(self, screen):
        circle(screen, (255, 0, 0), self.position.getTuple(), 30)
