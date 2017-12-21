import pygame

from tools.VecMath import Vec2D


class Game:
    time = pygame.time.Clock()
    UPDATE_SPEED = 0.001

    def __init__(self, window_dimension=None):
        from mechanics.Camera import Camera
        from Player import Player
        from mechanics.Obstacles import Platform
        self.window_dimension = window_dimension if window_dimension is not None else Vec2D(800, 600)
        self.screen = pygame.display.set_mode(self.window_dimension.get_tuple())
        self.camera = Camera(self.window_dimension)
        self.player = Player()
        self.platform = Platform()
        self.camera_setup()
        self.running = True
        self.run()

    def camera_setup(self):
        self.camera.add(self.player)
        self.camera.add(self.platform)
        self.camera.set_center(self.player)

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
            self.player.update()
            self.player.constrain(self.window_dimension)

            # Showing objects on the screen
            self.camera.show(self.screen, Vec2D(0, 0))
            self.camera.update()
            pygame.display.update()
