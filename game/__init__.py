import pygame
import time
import sys
from pygame.locals import *
from time import sleep
from game.Afficheur import Afficheur
pygame.init()

screen = pygame.display.set_mode((640, 480))
white = [247, 247, 247]
screen.fill(white)
surface = pygame.display.get_surface()
rex = pygame.image.load("images/rex/t-rex-start.png").convert_alpha()
ground = pygame.image.load("images/landscape/ground.png").convert_alpha()
ptera = pygame.image.load("images/ptera/ptera1.png").convert_alpha()
position_rex = rex.get_rect()
position_rex = position_rex.move(100,surface.get_height() - 43)
position_ground = ground.get_rect()
position_ground = position_ground.move(0,surface.get_height() - 15)
screen.blit(ground, position_ground)
screen.blit(rex ,position_rex)

pygame.display.flip()
pygame.key.set_repeat(400, 30)
continuer = 1
score = 0;


# def print_score(score):
#     score += 1
#     font = pygame.font.Font(None, 30)
#     scoretext = font.render("Score:" + str(score), 1, (0, 0, 0))
#     screen.blit(scoretext, (100,100))

def jump(position_rex):
    rex = pygame.image.load("images/rex/t-rex1.png").convert_alpha()
    for i in range(0, 150):
        if i < 75:
            position_rex = position_rex.move(0, -1)
            sleep(0.002)
        else:
            position_rex = position_rex.move(0, 1)
            sleep(0.002)
        screen.fill(white)
        screen.blit(ground, position_ground)
        screen.blit(rex, position_rex)
        pygame.display.flip()

def running(position_rex):
    rex = pygame.image.load("images/rex/t-rex3.png").convert_alpha()
    # rex.set_colorkey((255, 255, 255))
    screen.fill(white)
    screen.blit(ground, position_ground)
    screen.blit(rex, position_rex)
    pygame.display.flip()
    rex = pygame.image.load("images/rex/t-rex4.png").convert_alpha()
    screen.fill(white)
    screen.blit(ground, position_ground)
    screen.blit(rex, position_rex)
    pygame.display.flip()

def charge(position_rex):
    rex = pygame.image.load("images/rex/t-rex7.png").convert_alpha()
    screen.fill(white)
    screen.blit(ground, position_ground)
    screen.blit(rex, position_rex)
    pygame.display.flip()
    rex = pygame.image.load("images/rex/t-rex8.png").convert_alpha()
    screen.fill(white)
    screen.blit(ground, position_ground)
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
afficheur = Afficheur(score, screen, 1)
afficheur.start()
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
            afficheur._set_play(0)
        if event.type == KEYDOWN:
            if event.key == K_UP or event.key == K_SPACE:
                jump(position_rex)
                rex = pygame.image.load("images/rex/t-rex1.png").convert_alpha()
            if event.key == K_DOWN:
                down = 1
                position_rex = position_rex.move(0, 17)
                while down:
                    charge(position_rex)
                    score += 1
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            afficheur._set_play(0)
                            pygame.quit()
                            sys.exit()
                        if event.type == KEYUP and event.key == K_DOWN:
                            down = 0
                position_rex = position_rex.move(0, -17)
    running(position_rex)
    score += 1

