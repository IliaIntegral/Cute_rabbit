from Buttons import *

class UI:
    def __init__(self):
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0,255,0)
        self.blue = (0, 0, 255)
        self.dis = pygame.display.set_mode((Const.dis_width, Const.dis_height), pygame.FULLSCREEN)

    def draw(self, loc: Location, picture):
        self.dis.blit(picture, (loc.x, loc.y))

    def set_caption(self):
        pygame.display.set_caption('Cute rabbit game by II')

    def cycle(self, fal_obj, player, menu, start_from_paused, keyboard_paused):
        for object in fal_obj:
            self.draw(object.loc, object.picture)
        self.draw(player.loc, player.picture)
        self.draw(menu.loc, menu.picture)
        pygame.display.update()
        if keyboard_paused[0]:
            self.draw(start_from_paused.loc, start_from_paused.picture)
    def cycle_main_menu(self, start_playing, exit_from_main_menu):
        self.draw(start_playing.loc, start_playing.picture)
        self.draw(exit_from_main_menu.loc, exit_from_main_menu.picture)
        pygame.display.update()

    def cycle_go_to_main_menu(self, go_to_main_menu):
        self.draw(go_to_main_menu.loc, go_to_main_menu.picture)
        pygame.display.update()