import pygame
import sys
import random
from pygame.locals import *
from time import sleep
from game.Afficheur import Afficheur
from game.Ground import Ground
pygame.init()

screen = pygame.display.set_mode((1024, 480))
white = [247, 247, 247]
screen.fill(white)
surface = pygame.display.get_surface()
clock = pygame.time.Clock()

rex = pygame.image.load("images/rex/t-rex-start.png").convert_alpha()

#
# grounds = ["images/landscape/ground/ground1.png","images/landscape/ground/ground2.png","images/landscape/ground/ground3.png",
#               "images/landscape/ground/ground4.png","images/landscape/ground/ground5.png","images/landscape/ground/ground6.png",
#               "images/landscape/ground/ground7.png","images/landscape/ground/ground8.png","images/landscape/ground/ground9.png",
#               "images/landscape/ground/ground10.png","images/landscape/ground/ground11.png","images/landscape/ground/ground12.png",
#               "images/landscape/ground/ground13.png","images/landscape/ground/ground14.png","images/landscape/ground/ground15.png",
#               "images/landscape/ground/ground16.png","images/landscape/ground/ground17.png","images/landscape/ground/ground18.png",
#               "images/landscape/ground/ground19.png","images/landscape/ground/ground20.png","images/landscape/ground/ground21.png",
#               "images/landscape/ground/ground22.png","images/landscape/ground/ground23.png","images/landscape/ground/ground24.png"]

ground = [0]*64

# ground[0] = pygame.image.load(random.choice(grounds)).convert_alpha()
# position_ground = ground[0].get_rect()
# position_ground = position_ground.move(0, surface.get_height() - 15)
# for i in range(len(ground)):
#     ground[i] = pygame.image.load(random.choice(grounds)).convert_alpha()
#     screen.blit(ground[i], position_ground)
#     position_ground = position_ground.move(16, 0)

# ground = pygame.image.load("images/landscape/ground.png").convert_alpha()
ptera = pygame.image.load("images/ptera/ptera1.png").convert_alpha()
position_rex = rex.get_rect()
position_rex = position_rex.move(100,surface.get_height() - 43)
# position_ground = ground.get_rect()
# position_ground = position_ground.move(0,surface.get_height() - 15)
# screen.blit(ground, position_ground)
screen.blit(rex ,position_rex)

pygame.display.flip()
pygame.key.set_repeat(400, 30)
continuer = 1


# def print_score(score):
#     score += 1
#     font = pygame.font.Font(None, 30)
#     scoretext = font.render("Score:" + str(score), 1, (0, 0, 0))
#     screen.blit(scoretext, (100,100))

# def slide_ground():
#     position_ground = ground[0].get_rect()
#     position_ground = position_ground.move(0, surface.get_height() - 15)
#     for i in range(0, len(ground) - 1):
#         ground[i] = ground[i + 1]
#         screen.blit(ground[i], position_ground)
#         position_ground = position_ground.move(16, 0)
#     ground[len(ground) - 1] = pygame.image.load(random.choice(grounds)).convert_alpha()
#     screen.blit(ground[len(ground) - 1], position_ground)
#     screen.blit(rex, position_rex)
#     clock.tick(10)
#     pygame.display.flip()


def jump(position_rex):
    rex = pygame.image.load("images/rex/t-rex1.png").convert_alpha()
    for i in range(0, 150):
        if i < 75:
            position_rex = position_rex.move(0, -1)
        else:
            position_rex = position_rex.move(0, 1)
        screen.fill(white)
        screen.blit(rex, position_rex)
        pygame.display.flip()

def running(position_rex):
    rex = pygame.image.load("images/rex/t-rex3.png").convert_alpha()
    # rex.set_colorkey((255, 255, 255))
    screen.fill(white)
    screen.blit(rex, position_rex)
    clock.tick(10)
    pygame.display.flip()
    rex = pygame.image.load("images/rex/t-rex4.png").convert_alpha()
    screen.fill(white)
    screen.blit(rex, position_rex)
    clock.tick(10)
    pygame.display.flip()


def charge(position_rex):
    rex = pygame.image.load("images/rex/t-rex7.png").convert_alpha()
    screen.fill(white)
    screen.blit(rex, position_rex)
    clock.tick(10)
    pygame.display.flip()
    rex = pygame.image.load("images/rex/t-rex8.png").convert_alpha()
    screen.fill(white)
    screen.blit(rex, position_rex)
    clock.tick(10)
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
ground = Ground(screen,surface)
afficheur = Afficheur(screen)
start()
jump(position_rex)
afficheur.start()
ground.start()
while continuer:
    running(position_rex)
    # slide_ground()
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_UP or event.key == K_SPACE:
                jump(position_rex)
                rex = pygame.image.load("images/rex/t-rex1.png").convert_alpha()
            if event.key == K_DOWN:
                down = 1
                position_rex = position_rex.move(0, 17)
                while down:
                    charge(position_rex)
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            continuer = 0
                        if event.type == KEYUP and event.key == K_DOWN:
                            down = 0
                position_rex = position_rex.move(0, -17)
pygame.display.quit()
pygame.quit()
sys.exit()

