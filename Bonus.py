from Falling_Object import *


class Bonus(Falling_Object):
    def __init__(self, loc:Location, size: Size, picture, speed, duration, power):
        super().__init__(loc, size, picture,speed)
        self.duration = duration
        self.power = power
        self.type = type