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

    blancPng = "images/landscape/white.png"

    cactu = None
    surface = None
    play = True
    frame = None
    have_cactus = None

    white = (255, 255, 255)

    position_cactus = None
    position_draw = None

    def __init__(self, screen, surface):
        Thread.__init__(self)
        self.screen = screen
        self.surface = surface
        self.screen.get_rect()


    def slide_cactus(self):
        pygame.draw.rect(self.screen, self.white, self.position_cactus)
        self.position_cactus.left -= 16
        self.screen.blit(self.cactu, self.position_cactus)
        pygame.display.flip()
        self.clock.tick(20)
        if self.position_cactus.right < 0:
            self.have_cactus = None


    def print_cactus(self):
        self.cactu =  pygame.image.load(random.choice(self.cactus)).convert()
        self.cactu.set_colorkey((255,255,255))
        x = random.randint(0, 500)
        if x > 490:
            self.have_cactus = True
            self.position_cactus = self.cactu.get_rect(center=(self.surface.get_width() ,self.surface.get_height() - 30))
            self.screen.blit(self.cactu, self.position_cactus)


    def run(self):
        while self.play:
            if self.have_cactus == None:
                self.print_cactus()
            else :
                self.slide_cactus()

    def stop(self):
        self.play = False