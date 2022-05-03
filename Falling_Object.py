from Object import *


class Falling_Object(Object):
    def __init__(self, loc, size: Size, picture, speed):
        super().__init__(loc, size, picture, speed)
        self.picture = pygame.transform.scale(self.picture, (20,20))