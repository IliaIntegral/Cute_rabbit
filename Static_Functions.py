import Const
import Game_Controller
from Game_Controller import *
from Const import *
import time
from Game_Controller import *



def play_start_song():
    pygame.mixer.music.load('System_of_a_Down_Toxicity.mp3')
    pygame.mixer.music.play(-1, 0.0, 0)


def set_start_time():
    Const.start_time = int(time.time())

#def key_up(event, engine):
#    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#        engine.player_movement_ratio = (0, 0)