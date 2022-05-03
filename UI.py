import pygame
import Const
from Location import Location
from Size import Size
from Buttons import *

class UI:
    def __init__(self):
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0,255,0)
        self.blue = (0, 0, 255)
        self.dis = pygame.display.set_mode((Const.dis_width, Const.dis_height), pygame.FULLSCREEN)

    def draw(self, loc: Location, size: Size, picture):
        self.dis.blit(picture, (loc.x, loc.y))

    def set_caption(self):
        pygame.display.set_caption('Cute rabbit game by II')

    def cycle(self, fal_obj, player, menu):
        for object in fal_obj:
            self.draw(object.loc, object.size, object.picture)
        self.draw(player.loc, player.size, player.picture)
        self.draw(menu.loc, menu.size, menu.picture)
        menu.Button_action(print(22222222222222222222222222))
        pygame.display.update()

    #Biba boba
    #self.player_skin =
    #self.bigger_img = pygame.transform.scale(self.image, (int(self.size[0]*2), int(self.size[1]*2)))