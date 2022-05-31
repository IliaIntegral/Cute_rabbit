import pygame

from Game_Controller import *
from Player import Player
import Static_Functions


class Keyboard_Imput_Controller:
    def __init__(self):
        pass

    def get_events(self, events, engine, game_over, player: Player):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.key_down(event, engine, game_over, player)

    def key_down(self, event, engine, game_over, player):
        if event.key == pygame.K_LEFT:
            engine.move(player, -1 * player.speed[0], player.speed[1])
        elif event.key == pygame.K_RIGHT:
            engine.move(player, player.speed[0], player.speed[1])
        if event.key == pygame.K_q:
            game_over[0] = True

    def check_pressed(self, engine, player):
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            engine.move(player, player.speed[0], player.speed[1])
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            engine.move(player, -1 * player.speed[0], player.speed[1])
