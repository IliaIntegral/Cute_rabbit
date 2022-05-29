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

    def cycle(self, fal_obj, player, menu, start_from_paused, keyboard_paused):
        for object in fal_obj:
            self.draw(object.loc, object.size, object.picture)
        self.draw(player.loc, player.size, player.picture)
        self.draw(menu.loc, menu.size, menu.picture)
        if keyboard_paused[0]:
            self.draw(start_from_paused.loc, start_from_paused.size, start_from_paused.picture)


        #while paused:
         #   start = Buttons(Location(300, 200), Size(100, 100), "svet.png", 0)
          #  start.picture = pygame.transform.scale(start.picture, (100, 100))
           # self.dis.blit(start.picture, start.loc, start.size)
            #click = pygame.mouse.get_pressed()
            #if click[0] == 1:
              #  paused = False
        pygame.display.update()

    #self.player_skin =
    #self.bigger_img = pygame.transform.scale(self.image, (int(self.size[0]*2), int(self.size[1]*2)))