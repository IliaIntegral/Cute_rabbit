from Location import *
from Size import *
import pygame


class Object:
    def __init__(self, loc: Location, size: Size, picture, speed):
        self.loc = loc
        self.size = size
        self.picture = pygame.image.load(picture)
        self.speed = speed
        self.middle = [self.loc.x + self.size.width/2, self.loc.y + self.size.height/2]

