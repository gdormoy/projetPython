import pygame
from threading import Thread


class Afficheur(Thread):
    pygame.init()

    score = 0;
    screen = None
    position_score = None
    position_value = None
    scoretext = None
    scorevalue = None
    clock = pygame.time.Clock()
    white = (247, 247, 247)

    def __init__(self, screen):
        Thread.__init__(self)
        self.screen = screen
        font = pygame.font.SysFont('Verdana', 30)
        self.scoretext = font.render("Score:", 1, (1, 1, 1))
        self.scorevalue = font.render(str(self.score), 1, (1, 1, 1))
        self.position_score = self.scoretext.get_rect()
        self.position_score = self.position_score.move(700,100)
        self.position_value = self.scorevalue.get_rect()
        self.position_value = self.position_value.move(800,100)
        self.screen.blit(self.scoretext, self.position_score)
        self.screen.blit(self.scorevalue,self.position_value)
        pygame.display.update(self.position_score)
        pygame.display.update(self.position_value)

    def run(self):
        running = True
        font = pygame.font.SysFont('Verdana', 30)
        while running:
            self.score += 1
            pygame.draw.rect(self.screen, self.white, self.position_value)
            self.scorevalue = font.render(str(self.score), 1, (1, 1, 1))
            self.position_value = self.scorevalue.get_rect()
            self.position_value = self.position_value.move(800, 100)
            self.screen.blit(self.scorevalue, self.position_value)
            self.clock.tick(10)
            pygame.display.update(self.position_value)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False

