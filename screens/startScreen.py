import pygame
import os 
import configs.config as config
import dataBase.firebase_database as firebase_database

#create a block class
class StartScreen:
    SCREEN_WIDTH = config.SCREEN_WIDTH
    SCREEN_HEIGHT = config.SCREEN_HEIGHT
    INITIAL_IMAGE = config.INITIAL_IMAGE
    
    def __init__(self):
        self.screen = pygame.display.set_mode((StartScreen.SCREEN_WIDTH, StartScreen.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        font_path = config.FONT_PATH
        self.text_best_score = pygame.font.Font(font_path, 30).render(f'Best score: {firebase_database.getHighestScore()}', True, (0,0,0))
        self.text_rect_best_score = self.text_best_score.get_rect(center=(StartScreen.SCREEN_WIDTH // 2, (StartScreen.SCREEN_HEIGHT // 2 + 120)))
        
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
            self.screen.blit(StartScreen.INITIAL_IMAGE, (0, 0))
            self.screen.blit(self.text_best_score, (self.text_rect_best_score))

            # update the display
            pygame.display.flip()

            # wait for 1/60th of a second
            self.clock.tick(30)


        