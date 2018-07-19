import pygame
import random
from threading import Thread


class Ground(Thread):
    pygame.init()

    screen = None
    name = None
    clock = pygame.time.Clock()
    grounds = ["images/landscape/ground/ground1.png","images/landscape/ground/ground2.png","images/landscape/ground/ground3.png",
              "images/landscape/ground/ground4.png","images/landscape/ground/ground5.png","images/landscape/ground/ground6.png",
              "images/landscape/ground/ground7.png","images/landscape/ground/ground8.png","images/landscape/ground/ground9.png",
              "images/landscape/ground/ground10.png","images/landscape/ground/ground11.png","images/landscape/ground/ground12.png",
              "images/landscape/ground/ground13.png","images/landscape/ground/ground14.png","images/landscape/ground/ground15.png",
              "images/landscape/ground/ground16.png","images/landscape/ground/ground17.png","images/landscape/ground/ground18.png",
              "images/landscape/ground/ground19.png","images/landscape/ground/ground20.png","images/landscape/ground/ground21.png",
              "images/landscape/ground/ground22.png","images/landscape/ground/ground23.png","images/landscape/ground/ground24.png"]

    cactus = ["images/landscape/cactus/cactus1.png","images/landscape/cactus/cactus2.png","images/landscape/cactus/cactus3.png",
              "images/landscape/cactus/cactus4.png","images/landscape/cactus/cactus5.png","images/landscape/cactus/cactus6.png",
              "images/landscape/cactus/cactus7.png","images/landscape/cactus/cactus8.png","images/landscape/cactus/cactus9.png",
              "images/landscape/cactus/cactus10.png","images/landscape/cactus/cactus11.png","images/landscape/cactus/cactus12.png"]

    ground = [0]*64
    surface = None
    position_ground = None


    def __init__(self, screen, surface):
        Thread.__init__(self)
        self.screen = screen
        self.surface = surface
        self.ground[0] = pygame.image.load(random.choice(self.grounds)).convert_alpha()
        self.position_ground = self.ground[0].get_rect()
        self.position_ground = self.position_ground.move(0, self.surface.get_height() - 15)
        for i in range(len(self.ground)):
            self.ground[i] = pygame.image.load(random.choice(self.grounds)).convert_alpha()
            self.screen.blit(self.ground[i], self.position_ground)
            self.ground[i].set_colorkey((255, 255, 255))
            pygame.display.flip()
            self.position_ground = self.position_ground.move(16,0)
        pygame.display.flip()


    def slide_ground(self):
        self.position_ground = self.ground[0].get_rect()
        self.position_ground = self.position_ground.move(0, self.surface.get_height() - 15)
        for i in range(0, len(self.ground) - 1):
            self.ground[i] = self.ground[i + 1]
            self.ground[i].set_colorkey((255, 255, 255))
            self.screen.blit(self.ground[i], self.position_ground)
            pygame.display.flip()
            self.position_ground = self.position_ground.move(16, 0)
        self.ground[len(self.ground)-1] = pygame.image.load(random.choice(self.grounds)).convert_alpha()
        self.screen.blit(self.ground[len(self.ground)-1], self.position_ground)
        self.clock.tick(10)
        # pygame.display.flip()

    def run(self):
        play = True
        while play:
            self.slide_ground()
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()
            #         play = False

