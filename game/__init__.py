import pygame
import time
import sys
from pygame.locals import *
from time import sleep

pygame.init()

screen = pygame.display.set_mode((640, 480))
white = [247, 247, 247]
screen.fill(white)
surface = pygame.display.get_surface()
rex = pygame.image.load("images/rex/t-rex-start.png").convert_alpha()
# ptera = pygame.image.load("images/ptera/ptera1.png").convert_alpha()
position_rex = rex.get_rect()
position_rex = position_rex.move(100,surface.get_height() - 45)
screen.blit(rex ,position_rex)

pygame.display.flip()
pygame.key.set_repeat(400, 30)
continuer = 1

def jump(position_rex):
    rex = pygame.image.load("images/rex/t-rex1.png").convert_alpha()
    for i in range(0, 150):
        if i < 75:
            position_rex = position_rex.move(0, -1)
            sleep(0.003)
        else:
            position_rex = position_rex.move(0, 1)
            sleep(0.003)
        screen.fill(white)
        screen.blit(rex, position_rex)
        pygame.display.flip()

def running(position_rex):
    rex = pygame.image.load("images/rex/t-rex3.png").convert_alpha()
    screen.fill(white)
    screen.blit(rex, position_rex)
    pygame.display.flip()
    rex = pygame.image.load("images/rex/t-rex4.png").convert_alpha()
    screen.fill(white)
    screen.blit(rex, position_rex)
    pygame.display.flip()

def start():
    play = 1
    while play:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP or event.key == K_SPACE:
                    play = 0

start()
jump(position_rex)
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_UP or event.key == K_SPACE:
                jump(position_rex)
                rex = pygame.image.load("images/rex/t-rex1.png").convert_alpha()
    running(position_rex)