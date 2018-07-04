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
rexPosX =  100
rexPosY = surface.get_height() - 45
screen.blit(rex ,(rexPosX,rexPosY))

pygame.display.flip()

continuer = 1

while continuer:


    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN and event.key == K_UP:
            for i in range (0, 150):
                if i < 75:
                    rexPosY -= 1
                    sleep(0.003)
                else:
                    rexPosY += 1
                    sleep(0.003)
                screen.blit(rex, (rexPosX, rexPosY))
                pygame.display.flip()