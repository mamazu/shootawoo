import pygame
from VecMath import Vec2D

class Game:
    time = pygame.time.Clock()

    def __init__(self, window_dimension=None):
        from Camera import Camera
        from Player import Ball
        self.window_dimension = window_dimension if window_dimension is not None else Vec2D(800, 600)
        self.screen = pygame.display.set_mode(self.window_dimension.getTuple())
        self.camera = Camera()
        self.ball = Ball()
        self.camera.add(self.ball)
        self.running = True
        self.run()

    def catch_events(self, event_list):
        for event in event_list:
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_ESCAPE:
                    return False
        return True

    def run(self):
        while self.running:
            self.running = self.catch_events(pygame.event.get())

            # Updating positions
            self.ball.update()
            self.ball.constrain(self.window_dimension)

            # Showing objects on the screen
            self.camera.show(self.screen)
            pygame.display.update()
