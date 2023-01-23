import pygame.mouse
# from UI import UI
import Const
from Object import *
from Keyboard_Imput_Controller import *
class time_variable:
    def __init__(self, bool):
        self.bool = bool
#paused = time_variable(False)
class Buttons(Object):
    def __init__(self, loc: Location, size: Size, picture, speed):
        super().__init__(loc, size, picture, speed)
        self.picture = pygame.transform.scale(self.picture, (200, 200))
    def button_action_start_from_main_menu(self, game_menu):
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        if click[0] == 1 and self.loc.x < mouse[0] < self.loc.x + self.size.width and self.loc.y < mouse[1] < self.loc.y + self.size.height:
            game_menu[0] = False
    def button_action_go_to_main_menu(self, game_menu, paused):
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        if click[0] == 1 and self.loc.x < mouse[0] < self.loc.x + self.size.width and self.loc.y < mouse[1] < self.loc.y + self.size.height:
            if click[0] == 1:
                game_menu[0] = True
                paused[0] = False
    def button_action_start_from_pause(self, keyboard_paused):
        click = pygame.mouse.get_pressed()
        if click[0]:
            mouse = pygame.mouse.get_pos()
            if (self.loc.x < mouse[0]) and (mouse[0] < self.loc.x + self.size.width) and (self.loc.y < mouse[1]) and (mouse[1] < self.loc.y + self.size.height):
                keyboard_paused[0] = False
    def button_action_pause(self, keyboard_paused):
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        if click[0] == 1 and self.loc.x < mouse[0] < self.loc.x + self.size.width and self.loc.y < mouse[1] < self.loc.y + self.size.height:
            keyboard_paused[0] = True
    def button_action_exit_from_main_menu(self):
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        if click[0] == 1 and self.loc.x < mouse[0] < self.loc.x + self.size.width and self.loc.y < mouse[1] < self.loc.y + self.size.height:
            Const.game_over[0] = True
            #quit()