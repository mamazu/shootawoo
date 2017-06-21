import pygame

class Game:
    time = pygame.time.Clock()

    def __init__(self, dimension=None):
        from Camera import Camera
        from Player import Ball
        self.dimension = dimension if dimension is not None else (800, 600)
        self.screen = pygame.display.set_mode(self.dimension)
        self.camera = Camera()
        self.ball = Ball()
        self.camera.add(self.ball)
        self.running = True
        self.run()

    def catch_events(self, event_list):
        for event in event_list:
            if event.type == pygame.QUIT:
                return False
        return True

    def run(self):
        while self.running:
            self.running = self.catch_events(pygame.event.get())

            #Updating positions
            self.ball.update()

            #Rendering
            self.camera.show(self.screen)
            pygame.display.update()

            #Wait
            Game.time.tick(25)
