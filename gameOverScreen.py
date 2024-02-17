import pygame
import os
import config
import firebase_database

#create a block class
class GameOverScreen:
    SCREEN_WIDTH = config.SCREEN_WIDTH
    SCREEN_HEIGHT = config.SCREEN_HEIGHT

    def __init__(self, score):
        print(firebase_database.getHighestScore())
        font_path = config.FONT_PATH
        self.screen = pygame.display.set_mode((GameOverScreen.SCREEN_WIDTH, GameOverScreen.SCREEN_HEIGHT))
        self.score = score
        self.clock = pygame.time.Clock()
        self.text_score = pygame.font.Font(font_path, 36).render(f'Score: {self.score}', True, (0,0,0))
        self.text_best_score = pygame.font.Font(font_path, 36).render(f'Best score: {firebase_database.getHighestScore()}', True, (0,0,0))
        self.text_rect = self.text_score.get_rect(center=(GameOverScreen.SCREEN_WIDTH // 2, GameOverScreen.SCREEN_HEIGHT // 2))
        self.text_rect_best_score = self.text_best_score.get_rect(center=(GameOverScreen.SCREEN_WIDTH // 2, (GameOverScreen.SCREEN_HEIGHT // 2 + 25)))
        
    def run(self):

        self.running = True

        while self.running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.running = False
           

            # fill the screen with white
            self.screen.fill(("white"))
            self.screen.blit(self.text_score, (self.text_rect))
            self.screen.blit(self.text_best_score, (self.text_rect_best_score))

            # update the display
            pygame.display.flip()

            # wait for 1/60th of a second
            self.clock.tick(30)
        