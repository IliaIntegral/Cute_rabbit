from Object import *
from Location import *
from Falling_Object import *


class Fruit(Falling_Object):
    def __init__(self, loc: Location, size, speed, score, picture="Applepix.png"):
        super().__init__(loc, size, picture, speed)
        self.score = score