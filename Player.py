from Camera import Renderable
from pygame.draw import circle

class Ball(Renderable):
    def show(self, screen):
        circle(screen, (255, 0, 0), (200, 200), 30)
