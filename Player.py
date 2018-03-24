from pygame.rect import Rect

from mechanics.Camera import Renderable
from pygame.draw import circle

from Game import Game
from mechanics import Physics
from tools.VecMath import Vec2D


class Player(Renderable):
    def __init__(self):
        self.position = Vec2D(100, 200)
        self.speed = Vec2D(500, 0) * Game.UPDATE_SPEED
        self.acceleration = Vec2D(0, 1) * Game.UPDATE_SPEED
        self.radius = 30

    def update(self):
        self.speed += self.acceleration
        self.position += self.speed

    def constrain(self, window_dimension):
        if window_dimension.y < self.position.y + self.radius:
            self.bounce()

    def get_rect(self):
        top_left = self.position - self.radius
        return Rect(top_left.get_tuple(), (self.radius*2, self.radius*2))

    def bounce(self):
        self.speed.y *= -Physics.JUMP_DRAG

    def get_center(self):
        return self.position

    def show(self, screen, offset):
        position = self.position - offset
        circle(screen, (255, 0, 0), position.get_tuple(), self.radius)
