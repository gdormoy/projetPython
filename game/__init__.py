import pygame
import sys
from pygame.locals import *
from game.Score import Score
from game.Ground import Ground
from game.Rex import Rex
from game.Cactus import Cactus

pygame.init()

screen = pygame.display.set_mode((1024, 480))
white = (255, 255, 255)
screen.fill(white)
surface = pygame.display.get_surface()
clock = pygame.time.Clock()
#
rex = pygame.image.load("images/rex/t-rex-start.png").convert_alpha()
# screen_frame = pygame.Surface((screen.width, screen.height))
ptera = pygame.image.load("images/ptera/ptera1.png").convert_alpha()
position_rex = rex.get_rect()
position_rex = position_rex.move(100,surface.get_height() - 50)
screen.blit(rex ,position_rex)

pygame.key.set_repeat(400, 30)
game = 1
game = 1



def jump(position_rex):
    rex = pygame.image.load("images/rex/t-rex1.png").convert_alpha()
    frame = pygame.Surface((position_rex.width, position_rex.height))
    for i in range(0, 280):
        frame.fill(white)
        screen.blit(frame, position_rex)
        if i < 100:
            position_rex = position_rex.move(0, -1)
        elif i > 180 :
            position_rex = position_rex.move(0, 1)
        rex.set_colorkey((255, 255, 255))
        rex.set_colorkey((255, 255, 255))
        screen.blit(rex, position_rex)
        clock.tick(500)
        pygame.display.flip()

def running(position_rex):
    rex = pygame.image.load("images/rex/t-rex3.png").convert_alpha()
    rex.set_colorkey((255, 255, 255))
    screen.blit(rex, position_rex)
    clock.tick(10)
    pygame.display.flip()
    rex = pygame.image.load("images/rex/t-rex4.png").convert_alpha()
    rex.set_colorkey((255, 255, 255))
    screen.blit(rex, position_rex)
    clock.tick(10)
    pygame.display.flip()


def charge(position_rex):
    rex = pygame.image.load("images/rex/t-rex7.png").convert_alpha()
    rex.set_colorkey((255, 255, 255))
    screen.blit(rex, position_rex)
    clock.tick(10)
    pygame.display.flip()
    rex = pygame.image.load("images/rex/t-rex8.png").convert_alpha()
    rex.set_colorkey((255, 255, 255))
    screen.blit(rex, position_rex)
    clock.tick(10)
    pygame.display.flip()
    frame = pygame.Surface((position_rex.width ,position_rex.height))
    frame.fill(white)
    screen.blit(frame, position_rex)

def start():
    play = 1
    while play:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP or event.key == K_SPACE:
                    jump(position_rex)
                    play = 0

cactus = Cactus(screen,surface)
ground = Ground(screen,surface)
score = Score(screen)
start()
cactus.start()
pygame.display.flip()
score.start()
ground.start()
while game:
    running(position_rex)
    pygame.display.update(screen.get_rect())
    if position_rex.colliderect(cactus.position_cactus) == 1:
        game = 0
        ground.stop()
        score.stop()
        cactus.stop()
        print("score : {}".format(score.score))
    for event in pygame.event.get():
        if event.type == QUIT:
            game = 0
        if event.type == KEYDOWN:
            if event.key == K_UP or event.key == K_SPACE:
                jump(position_rex)
                rex = pygame.image.load("images/rex/t-rex1.png").convert_alpha()
            if event.key == K_DOWN:
                down = 1
                frame = pygame.Surface((position_rex.width, position_rex.height))
                frame.fill(white)
                screen.blit(frame, position_rex)
                position_rex = position_rex.move(0, 17)
                while down:
                    # rex.charge()
                    charge(position_rex)
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            game = 0
                        if event.type == KEYUP and event.key == K_DOWN:
                            down = 0
                position_rex = position_rex.move(0, -17)

# pygame.display.quit()
# pygame.quit()
# sys.exit()

