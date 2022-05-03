import pygame.mouse
# from UI import UI
import Const
from Object import *


class Buttons(Object):
    def __init__(self, loc: Location, size: Size, picture, speed):
        super().__init__(loc, size, picture, speed)
        self.picture = pygame.transform.scale(self.picture, (20, 20))
        # self.picture = pygame.image.load(picture)
        self.dis = pygame.display.set_mode((Const.dis_width, Const.dis_height), pygame.FULLSCREEN)
        self.click = pygame.mouse.get_pressed()

    def button_action(self, action):
        # if self.click[0] == 1:
        action()
