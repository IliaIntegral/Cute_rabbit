import Const
from Game_Field import *

class Engine:
    def __init__(self, game_field: Game_Field = Game_Field(Player("pixil-fra(5).png"))):
        self.game_field = game_field
        #self.player_movement_ratio = (1,0)
        #self.objects_falling_ratio = (0,2)

    def move(self, object: Object, x_change, y_change):
        if (object.loc.x > 0) and (object.loc.x + object.size.width < Const.dis_width):
            object.loc.x += x_change
            object.loc.y += y_change
            object.middle[0] += x_change
            object.middle[1] += y_change
        else:
            if object.loc.x <= 0:
                object.loc.x = Const.dis_width-object.size.width-1
                object.middle[0] = Const.dis_width-object.size.width-1

            if object.loc.x >= Const.dis_width - object.size.width:
                object.loc.x = 1
                object.middle[0] = 1