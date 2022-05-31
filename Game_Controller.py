import pygame
import Songs
import Static_Functions
import time
import random
import Const
from Buttons import Buttons
from Size import Size
from Location import Location
from Engine import Engine
from UI import UI
from Buttons import *
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



        # Static_Functions.play_start_song()
        self.ui.set_caption()

        self.pause = Buttons(Location(50, 50), Size(100, 100), "pause.png", [0, 0])
        self.pause.picture = pygame.transform.scale(self.pause.picture, (100, 100))

        self.start_from_paused = Buttons(Location(300, 300), Size(100, 100), "start_from_paused.png", [0, 0])
        self.start_from_paused.picture = pygame.transform.scale(self.start_from_paused.picture, (100, 100))

        self.start_playing_from_main_menu = Buttons(Location(500, 300), Size(641, 389), "start_playing.png", [0, 0])
        self.start_playing_from_main_menu.picture = pygame.transform.scale(self.start_playing_from_main_menu.picture, (641, 389))

        self.go_to_main_menu = Buttons(Location(300, 500), Size(200, 200), "go_to_main_menu_from_paused.png", [0, 0])
        self.go_to_main_menu.picture = pygame.transform.scale(self.go_to_main_menu.picture, (200, 200))

        self.exit_from_main_menu = Buttons(Location(300, 100), Size(200, 200), "exit_from_main_menu.png", [0, 0])
        self.exit_from_main_menu.picture = pygame.transform.scale(self.exit_from_main_menu.picture, (200, 200))


        keyboard_paused = [False]
        game_over = [False]
        game_menu = [False]
        clock = pygame.time.Clock()



        while not game_over[0]:
            if game_menu[0]:
                self.main_menu(game_menu, game_over)
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

            self.ui.cycle(self.engine.game_field.fal_objects, self.engine.game_field.player, self.pause, self.start_from_paused, keyboard_paused)
            self.pause.button_action_pause(keyboard_paused)
            if keyboard_paused[0]:
                self.paused_in_game(keyboard_paused, game_menu)
            clock.tick(30)


        print(self.engine.game_field.player.score)
        pygame.quit()
        quit()

    def main_menu(self, game_menu, game_over):
        for object in self.engine.game_field.fal_objects:
                self.engine.game_field.player.score = 0
                self.engine.game_field.fal_objects.remove(object)
        while game_menu[0]:
            self.ui.dis.fill((0, 0, 255))
            self.ui.cycle_main_menu(self.start_playing_from_main_menu, self.exit_from_main_menu)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.display.update()
            self.start_playing_from_main_menu.button_action_start_from_main_menu(game_menu)
            self.exit_from_main_menu.button_action_exit_from_main_menu(game_over)
    def paused_in_game(self, keyboard_paused, game_menu):
        while keyboard_paused[0] == True:
            self.ui.cycle(self.engine.game_field.fal_objects, self.engine.game_field.player, self.pause,  self.start_from_paused, keyboard_paused)
            self.start_from_paused.button_action_start_from_pause(keyboard_paused)
            self.ui.cycle_go_to_main_menu(self.go_to_main_menu)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.display.update()
            self.go_to_main_menu.button_action_go_to_main_menu(game_menu, keyboard_paused)
