import pygame
def play_start_song():
    pygame.mixer.music.load('Рингтон.mp3')
    pygame.mixer.music.play(-1, 0.0, 0)