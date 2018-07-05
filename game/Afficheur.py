import pygame
from threading import Thread

class Afficheur(Thread):

    score = 0;
    screen = None
    play = 0

    def __init__(self, score, screen, play):
        Thread.__init__(self)
        self.score = score
        self.screen = screen
        self.play = play

    def _set_play(self, play):
        self.play = play

    def run(self):
        while self.play:
            self.score += 1
            font = pygame.font.Font(None, 30)
            scoretext = font.render("Score:" + str(self.score), 1, (0, 0, 0))
            self.screen.blit(scoretext, (100,100))
            pygame.display.flip()
