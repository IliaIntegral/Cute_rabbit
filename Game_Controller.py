import pygame
import Songs
import Static_Functions
import time
import random
import Const
from Size import Size
from Location import Location
from Engine import Engine
from UI import UI
from Buttons import Buttons
from Collision_Controller import Collision_Controller
from Fall_Controller import Fall_Controller
from Spawn_Controller import Spawn_Controller
from Keyboard_Imput_Controller import Keyboard_Imput_Controller


class Game_Controller:
    def __init__(self):

        pygame.init()
        Static_Functions.set_start_time()

        self.col_cont = Collision_Controller()
        self.fall_cont = Fall_Controller()
        self.spawn_cont = Spawn_Controller()
        self.keyboard_imput_cont = Keyboard_Imput_Controller()
        self.ui = UI()
        self.engine = Engine()

        Static_Functions.play_start_song()
        self.ui.set_caption()

        self.menu = Buttons(Location(50, 50), Size(50, 50), "pause.png", [0, 0])
        self.menu.picture = pygame.transform.scale(self.menu.picture, (100, 100))




        game_over = [False]
        clock = pygame.time.Clock()
        while not game_over[0]:

            events = pygame.event.get()
            self.keyboard_imput_cont.get_events(events, self.engine, game_over, self.engine.game_field.player)

            self.ui.dis.fill((247, 247, 247))

            self.keyboard_imput_cont.check_pressed(self.engine, self.engine.game_field.player)

            if random.randint(1, 10000) <= self.spawn_cont.spawn_chance:
                self.spawn_cont.spawn_obj(self.engine.game_field.fal_objects)
                self.spawn_cont.num_obj += 1
                if self.spawn_cont.num_obj == self.spawn_cont.num_obj_to_decrease_period and self.spawn_cont.spawn_chance < 1000:
                    self.spawn_cont.spawn_chance += 10
                    self.spawn_cont.num_obj = 0

            self.fall_cont.set_fall_speed(self.engine.game_field.fal_objects)
            self.fall_cont.move_fall_objects(self.engine.game_field.fal_objects, self.engine)
            self.fall_cont.check_fall(self.engine.game_field.fal_objects, self.engine.game_field.player, game_over)

            self.col_cont.check_collision(self.engine.game_field.fal_objects, self.engine.game_field.player)

            self.ui.cycle(self.engine.game_field.fal_objects, self.engine.game_field.player, self.menu)


            clock.tick(30)

        print(self.engine.game_field.player.score)
        pygame.quit()
        quit()