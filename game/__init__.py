import pygame
from pygame.locals import *

pygame.init()


screen = pygame.display.set_mode((640, 480))
white = [255, 255, 255]
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
            for i in range (0, 200):
                if i < 100:
                    rexPosY -= 1
                else:
                    rexPosY += 1
                screen.blit(rex, (rexPosX, rexPosY))
                pygame.display.flip()