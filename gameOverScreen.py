import pygame
import os
import config

#create a block class
class GameOverScreen:
    SCREEN_WIDTH = config.SCREEN_WIDTH
    SCREEN_HEIGHT = config.SCREEN_HEIGHT

    def __init__(self, score):
        self.screen = pygame.display.set_mode((GameOverScreen.SCREEN_WIDTH, GameOverScreen.SCREEN_HEIGHT))
        self.score = score
        self.clock = pygame.time.Clock()
        self.text = pygame.font.Font(None, 36).render(f'Score: {self.score}', True, (0,0,0))
        self.text_rect = self.text.get_rect(center=(GameOverScreen.SCREEN_WIDTH // 2, GameOverScreen.SCREEN_HEIGHT // 2))
        
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
            self.screen.blit(self.text, (self.text_rect))

            # update the display
            pygame.display.flip()

            # wait for 1/60th of a second
            self.clock.tick(30)


        