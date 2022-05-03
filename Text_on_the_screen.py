import dis

from Object import *
import pygame
import Const
class Text_on_the_screen():
    def __init__(self, text, loc : Location, size : Size, dis):
        self.text = text
        self.loc = loc
        self.size = size
        self.dis = pygame.display.set_mode((Const.dis_width, Const.dis_height), pygame.FULLSCREEN)
    def print_text(self):
        self.dis.blit(self.text, self.loc)
