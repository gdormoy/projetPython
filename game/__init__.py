import pygame
import time

from pygame.locals import *
from time import sleep

pygame.init()


screen = pygame.display.set_mode((640, 480))
white = [247, 247, 247]
screen.fill(white)
surface = pygame.display.get_surface()
rex = pygame.image.load("images/t-rex.png").convert_alpha()
position_rex = rex.get_rect()
position_rex = position_rex.move(100,surface.get_height() - 45)
screen.blit(rex ,position_rex)

pygame.display.flip()

continuer = 1

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_UP or event.key == K_SPACE:
                for i in range (0, 150):
                    if i < 75:
                        position_rex = position_rex.move(0, -1)
                        sleep(0.003)
                    else:
                        position_rex = position_rex.move(0, 1)
                        sleep(0.003)
                    screen.blit(rex, position_rex)
                    pygame.display.flip()