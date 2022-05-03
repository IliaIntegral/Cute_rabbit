class Fall_Controller:
    def __init__(self):
        self.fall_speed = (0,5)
        self.num_fallen_obj = 0


    def set_fall_speed(self,fall_objects):
        for object in fall_objects:
            object.speed = self.fall_speed

    def move_fall_objects(self, fall_objects, engine):
        for object in fall_objects:
            engine.move(object, object.speed[0], object.speed[1])

    def check_fall(self, fall_objects, player, game_over):
        for object in fall_objects:
            if object.loc.y == 800:
                player.score -= object.score
                self.num_fallen_obj += 1
                fall_objects.remove(object)
        if self.num_fallen_obj == 5:
            game_over[0] = True