from abc import abstractmethod

class Renderable:

    @abstractmethod
    def show(self, screen):
        print('Implement show method')

class Camera(Renderable):
    def __init__(self):
        self.background = (0, 128, 0)
        self.objects = []

    def add(self, camera_object):
        if isinstance(camera_object, Renderable):
            self.objects.append(camera_object)
        else:
            print("Object is not renderable: %s" % camera_object.__class__)

    def show(self, screen):
        screen.fill(self.background)
        for obj in self.objects:
            obj.show(screen)
