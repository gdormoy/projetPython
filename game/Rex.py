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
    clock = pygame.time.Clock()

    def __init__(self, screen, surface):
        Thread.__init__(self)
        self.screen = screen
        self.surface = surface
        self.rex = pygame.image.load("images/rex/t-rex-start.png").convert_alpha()
        self.position_rex = self.rex.get_rect()
        self.position_rex = self.position_rex.move(100, surface.get_height() - 43)
        pygame.display.update(self.rex.get_rect())

    def jump(self):
        self.rex = pygame.image.load("images/rex/t-rex1.png").convert_alpha()
        for i in range(0, 150):
            if i < 75:
                self.position_rex = self.position_rex.move(0, -1)
            else:
                self.position_rex = self.position_rex.move(0, 1)
            self.screen.blit(self.rex, self.position_rex)
            pygame.display.update(self.rex.get_rect())

    def running(self):
        self.rex = pygame.image.load("images/rex/t-rex3.png").convert_alpha()
        # rex.set_colorkey((255, 255, 255))
        self.screen.blit(self.rex, self.position_rex)
        self.clock.tick(10)
        pygame.display.update(self.rex.get_rect())
        self.rex = pygame.image.load("images/rex/t-rex4.png").convert_alpha()
        self.screen.blit(self.rex, self.position_rex)
        self.clock.tick(10)
        pygame.display.update(self.rex.get_rect())

    def charge(self):
        self.rex = pygame.image.load("images/rex/t-rex7.png").convert_alpha()
        self.screen.blit(self.rex, self.position_rex)
        self.clock.tick(10)
        pygame.display.update(self.rex.get_rect())
        self.rex = pygame.image.load("images/rex/t-rex8.png").convert_alpha()
        self.screen.blit(self.rex, self.position_rex)
        self.clock.tick(10)
        pygame.display.update(self.rex.get_rect())

    def run(self):
        running = True
        while running:
            self.running()
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == KEYDOWN:
                    if event.key == K_UP or event.key == K_SPACE:
                        self.jump()
                        self.rex = pygame.image.load("images/rex/t-rex1.png").convert_alpha()
                    if event.key == K_DOWN:
                        down = 1
                        self.position_rex = self.position_rex.move(0, 17)
                        while down:
                            self.charge()
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    running = False
                                if event.type == KEYUP and event.key == K_DOWN:
                                    down = 0
                        self.position_rex = self.position_rex.move(0, -17)

