from Camera import Renderable
from pygame.draw import circle, rect
from VecMath import Vec2D

class Ball(Renderable):
    def __init__(self):
        self.position = Vec2D(400, 200)
        self.speed = Vec2D(0, 0)
        self.acceleration = Vec2D(0, 0.001)
        self.radius = 30

    def update(self):
        self.speed += self.acceleration
        self.position += self.speed

    def constrain(self, window_dimension):
        if window_dimension.y < self.position.y + self.radius:
            self.speed *= -1

    def show(self, screen):
        circle(screen, (255, 0, 0), self.position.getTuple(), self.radius)
