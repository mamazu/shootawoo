import Physics

from Game import Game
from Camera import Renderable
from pygame.draw import circle, rect
from VecMath import Vec2D

class Ball(Renderable):
    def __init__(self):
        self.position = Vec2D(100, 200)
        self.speed = Vec2D(100, 0) * Game.UPDATE_SPEED
        self.acceleration = Vec2D(0, 1) * Game.UPDATE_SPEED
        self.radius = 30

    def update(self):
        self.speed += self.acceleration
        self.position += self.speed

    def constrain(self, window_dimension):
        if window_dimension.y < self.position.y + self.radius:
            self.speed.y *= -Physics.JUMP_DRAG

    def show(self, screen):
        circle(screen, (255, 0, 0), self.position.getTuple(), self.radius)
