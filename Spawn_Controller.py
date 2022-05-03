import random
from Location import  Location
import Const
from Size import Size

from Fruit import Fruit

class Spawn_Controller:
    def __init__(self):
        self.spawn_chance = 300         #50 - не 50%. Используется здесь: if random.randint(1,10000) <= self.spawn_cont.spawn_chance:
                                        # (Game_Controller)
        self.num_obj_to_decrease_period = 8
        self.num_obj = 0


    def spawn_obj(self, fal_obj):
        new_obj = Fruit(Location(random.randint(100, Const.dis_width-100), 100), Size(20, 20), [0, 5], 10)
        fal_obj.append(new_obj)