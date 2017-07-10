from abc import abstractmethod, ABCMeta

from Game import Game
from tools.VecMath import Vec2D


class Renderable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def show(self, screen, offset):
        print('Implement show method')


class Camera(Renderable):
    def __init__(self):
        self.background = (0, 128, 0)
        self.position = Vec2D(0, 0)
        self.objects = []
        self.center_object = None

    def add(self, camera_object):
        if isinstance(camera_object, Renderable):
            self.objects.append(camera_object)
        else:
            print("Object is not renderable: %s" % camera_object.__class__)

    def show(self, screen, offset):
        screen.fill(self.background)
        offset = self.position + offset
        for obj in self.objects:
            obj.show(screen, offset)

    def update(self):
        self.position += Vec2D(50 * Game.UPDATE_SPEED, 0)
