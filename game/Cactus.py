import pygame
import random
from threading import Thread


class Cactus(Thread):
    pygame.init()

    screen = None
    name = None
    clock = pygame.time.Clock()

    cactus = ["images/landscape/cactus/cactus1.png", "images/landscape/cactus/cactus2.png",
              "images/landscape/cactus/cactus3.png",
              "images/landscape/cactus/cactus4.png", "images/landscape/cactus/cactus5.png",
              "images/landscape/cactus/cactus6.png",
              "images/landscape/cactus/cactus7.png", "images/landscape/cactus/cactus8.png",
              "images/landscape/cactus/cactus9.png",
              "images/landscape/cactus/cactus10.png", "images/landscape/cactus/cactus11.png",
              "images/landscape/cactus/cactus12.png"]

    cactu = [0] * 64
    surface = None
    position_cactus = None
    white = (255, 255, 255)

    def __init__(self, screen, surface):
        Thread.__init__(self)
        self.screen = screen
        self.surface = surface
        self.cactu[0] = pygame.image.load(random.choice(self.cactus)).convert_alpha()
        self.position_cactus = self.cactu[0].get_rect()
        self.position_cactus = self.position_cactus.move(0, self.surface.get_height() - 15)
        for i in range(len(self.cactu)):
            self.cactu[i] = pygame.image.load(random.choice(self.cactus)).convert_alpha()
            self.screen.blit(self.cactu[i], self.position_cactus)
            self.cactu[i].set_colorkey((255, 255, 255))
            pygame.display.flip()
            self.position_cactus = self.position_cactus.move(16,0)
        pygame.display.flip()


    def slide_cactus(self):
        i = random.randint(0, 50)
        print(i)
        self.position_cactus = self.cactu[0].get_rect()
        self.position_cactus = self.position_cactus.move(0, self.surface.get_height() - 50)
        for i in range(0, len(self.cactu) - 1):
            self.cactu[i] = self.cactu[i + 1]
            self.cactu[i].set_colorkey((255, 255, 255))
            self.screen.blit(self.cactu[i], self.position_cactus)
            pygame.display.flip()
            self.position_cactus = self.position_cactus.move(16, 0)
        if i == 50 :
            self.cactu[len(self.cactu) - 1] = pygame.image.load(random.choice(self.cactus)).convert_alpha()
        else:
            frame = pygame.Surface((self.position_cactus.width, self.position_cactus.height))
            frame.fill(self.white)
            self.cactu[len(self.cactu) - 1] = frame
        self.screen.blit(self.cactu[len(self.cactu)-1], self.position_cactus)
        self.clock.tick(10)
        # pygame.display.flip()

    def run(self):
        play = True
        while play:
            self.slide_cactus()