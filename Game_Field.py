from Player import *
from Falling_Object import *


class Game_Field:
    def __init__(self, player: Player):
        self.fal_objects = []
        self.player = player