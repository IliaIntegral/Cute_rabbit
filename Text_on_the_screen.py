"""
import dis

from Object import *
import pygame
import Const
class Text_on_the_screen():
    def __init__(self, massage, loc : Location, size : Size, pic):
        self.massage = massage
        self.loc = loc
        self.size = size
        self.dis = pygame.display.set_mode((Const.dis_width, Const.dis_height), pygame.FULLSCREEN)
        self.font_type = pygame.font.Font("PakenhamBl Italic.ttf", 45)
        self.text = self.font_type.render(self.massage, True, (0, 0, 0))
        self.pic = pic
    def print_text(self):
        self.dis.blit(self.pic, self.loc)"""
