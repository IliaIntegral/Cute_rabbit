from Location import *
from Object import *
from Fruit import *
from Bonus import *


class Player(Object):
    def __init__(self, picture, loc: Location = Location(600, 700), speed=[20,0], score=0, hp=100, size=Size(100,100)):
        super().__init__(loc, size, picture, speed)
        self.hp = hp
        self.score = score
        self.speed = speed
        self.picture = pygame.transform.scale(self.picture, (100,100))