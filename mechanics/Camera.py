from abc import abstractmethod, ABCMeta

from tools.VecMath import Vec2D


class Renderable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def show(self, screen, offset):
        print('Implement show method')


class Camera(Renderable):
    def __init__(self, size):
        self.background = (0, 128, 0)
        self.position = Vec2D(0, 0)
        self.size = size
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
        if self.center_object is None:
            return
        ball_center = self.center_object.get_center()  # type: Vec2D
        new_position = ball_center - self.size / 2
        new_position.clamp_y(None, 0)
        new_position.clamp_x(0)
        self.smooth_update(new_position, .01)

    def smooth_update(self, new_position, speed):
        distance = new_position - self.position
        self.position += distance * speed

    def set_center(self, center_object):
        self.center_object = center_object
