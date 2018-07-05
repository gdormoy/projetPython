import pygame
from threading import Thread


class Afficheur(Thread):
    pygame.init()


    score = 0;
    screen = None
    clock = pygame.time.Clock()

    def __init__(self, screen):
        Thread.__init__(self)
        self.screen = screen
        font = pygame.font.SysFont('Verdana', 30)
        scoretext = font.render("Score:" + str(self.score), 1, (1, 1, 1))
        self.screen.blit(scoretext, (700, 100))
        pygame.display.update(scoretext.get_rect())

    def run(self):
        running = True
        while running:
            self.score += 1
            font = pygame.font.SysFont('Verdana', 30)
            scoretext = font.render("Score:" + str(self.score), 1, (1, 1, 1))
            self.screen.blit(scoretext, (700,100))
            self.clock.tick(10)
            pygame.display.update(scoretext.get_rect())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False

