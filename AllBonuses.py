from Bonus import *


class SizeDownBonus(Bonus):
    def __init__(self, loc: Location, size: Size, picture, speed, duration, power):
        super().__init__(loc, size, picture, speed, duration, power)