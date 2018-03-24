from pygame.rect import Rect
from tools.VecMath import Vec2D
from pygame.draw import rect
from Camera import Renderable
from random import randrange


class Block(Renderable):
    def __init__(self, position, size):
        self.position = position if Vec2D.isVec(position) else Vec2D(0, 0)
        self.size = size if Vec2D.isVec(size) else Vec2D(10, 10)

    def is_visible(self, minimum_x=0):
        return self.get_right_edge().x > minimum_x

    def get_right_edge(self):
        return self.position + self.size

    def collides(self, other_renerable):
        self_rect = self.get_rect()
        other_rect = other_renerable.get_rect()
        if self_rect.colliderect(other_rect):
            other_renerable.position.y = self_rect.top - other_rect.height
            return other_rect.left + other_rect.width // 2 >= self_rect.left

    def get_rect(self):
        return Rect(self.position.get_tuple(), self.size.get_tuple())

    def show(self, screen, offset):
        pos_x, pos_y = (self.position - offset).get_tuple()
        size_x, size_y = self.size.get_tuple()
        rect(screen, (0, 0, 0), (pos_x, pos_y, size_x, size_y))


class Level(Renderable):
    def __init__(self, dimension):
        self.dimension = dimension
        self.blocks = [
            Block(Vec2D(0, 400), Vec2D(100, 300))
        ]
        self.x_offset = 0

    def update(self):
        self.remove_invisible_blocks()

        # Generate new platforms
        current = self.blocks[-1].get_right_edge().x
        end = self.x_offset + self.dimension.x * 1.2
        height = 50

        while current <= end:
            current += self.get_distance_between_blocks()
            width = randrange(80, 100)
            block = Block(Vec2D(current, self.dimension.y - height), Vec2D(width, height))
            self.blocks.append(block)
            current += width

    def remove_invisible_blocks(self):
        padding = self.x_offset - self.dimension.x * 0.2
        self.blocks = [block for block in self.blocks if block.is_visible(padding)]

    def get_distance_between_blocks(self):
        difficulty = max(1.0, self.x_offset / 1000)
        return int(randrange(30, 70) * difficulty)

    def collides(self, other_rederable):
        for block in self.blocks:
            if block.collides(other_rederable):
                return True

        return False

    def show(self, screen, offset):
        self.x_offset = offset.x
        for block in self.blocks:
            block.show(screen, offset)
