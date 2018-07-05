import pygame
from threading import Thread
from pygame.locals import *


class Rex(Thread):
    pygame.init()

    screen = None
    name = None
    rex = None
    surface = None
    position_rex = None
    white = (247, 247, 247)
    clock = pygame.time.Clock()

    def __init__(self, screen, surface):
        Thread.__init__(self)
        self.screen = screen
        self.surface = surface
        self.rex = pygame.image.load("images/rex/t-rex-start.png").convert_alpha()
        self.rex.set_colorkey((247, 247, 247))
        self.position_rex = self.rex.get_rect()
        self.position_rex = self.position_rex.move(100, surface.get_height() - 43)
        self.screen.blit(self.rex, self.position_rex)
        pygame.display.update(self.position_rex)

    def jump(self):
        self.rex = pygame.image.load("images/rex/t-rex1.png").convert_alpha()
        frame = pygame.Surface((self.position_rex.width, self.position_rex.height))
        for i in range(0, 180):
            frame.fill(self.white)
            self.screen.blit(frame, self.position_rex)
            self.rex.set_colorkey((247, 247, 247))
            if i < 90:
                self.position_rex = self.position_rex.move(0, -1)
            else:
                self.position_rex = self.position_rex.move(0, 1)
                self.screen.blit(self.rex, self.position_rex)
                self.clock.tick(200)
            pygame.display.flip()

    def walk(self):
        self.rex = pygame.image.load("images/rex/t-rex3.png").convert_alpha()
        self.rex.set_colorkey((247, 247, 247))
        self.screen.blit(self.rex, self.position_rex)
        self.clock.tick(10)
        pygame.display.flip()
        self.rex = pygame.image.load("images/rex/t-rex4.png").convert_alpha()
        self.rex.set_colorkey((247, 247, 247))
        self.screen.blit(self.rex, self.position_rex)
        self.clock.tick(10)
        pygame.display.flip()

    def charge(self):
        frame = pygame.Surface((self.position_rex.width, self.position_rex.height))
        frame.fill(self.white)
        self.screen.blit(frame, self.position_rex)
        self.position_rex = self.rex.get_rect()
        self.position_rex = self.position_rex.move(100, self.surface.get_height() - 26)
        self.rex = pygame.image.load("images/rex/t-rex7.png").convert_alpha()
        self.rex.set_colorkey((247, 247, 247))
        self.screen.blit(self.rex, self.position_rex)
        self.clock.tick(10)
        pygame.display.flip()
        self.rex = pygame.image.load("images/rex/t-rex8.png").convert_alpha()
        self.rex.set_colorkey((247, 247, 247))
        self.screen.blit(self.rex, self.position_rex)
        self.clock.tick(10)
        pygame.display.flip()
        self.position_rex = self.rex.get_rect()
        self.position_rex = self.position_rex.move(100, self.surface.get_height() - 43)
        frame2 = pygame.Surface((self.position_rex.width, self.position_rex.height))
        frame2.fill(self.white)
        self.screen.blit(frame2, self.position_rex)

    def run(self):
        play = True
        while play:
            # self.running()
            for event in pygame.event.get():
                if event.type == QUIT:
                    play = False
                # if event.type == KEYDOWN:
                #     if event.key == K_UP or event.key == K_SPACE:
                #         self.jump()
                #         self.rex = pygame.image.load("images/rex/t-rex1.png").convert_alpha()
                #     if event.key == K_DOWN:
                #         down = 1
                #         self.position_rex = self.position_rex.move(0, 17)
                #         while down:
                #             self.charge()
                #             for event in pygame.event.get():
                #                 if event.type == QUIT:
                #                     play = False
                #                 if event.type == KEYUP and event.key == K_DOWN:
                #                     down = 0
                #         self.position_rex = self.position_rex.move(0, -17)

