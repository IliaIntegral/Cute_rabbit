from Fruit import Fruit

class Collision_Controller:
    def __init__(self):
        pass

    def check_collision(self, fal_obj, player):
        for object in fal_obj:
            if (abs(player.middle[0]-object.middle[0]) <= (player.size.width+object.size.width) / 2) and (abs(player.middle[1]-object.middle[1]) <= (player.size.height+object.size.height) / 2):
                if type(object) == Fruit:
                    player.score += object.score
                    fal_obj.remove(object)