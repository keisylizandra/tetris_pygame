import pygame
import os
import config
import firebase_database

class PauseScreen:
    SCREEN_WIDTH = config.SCREEN_WIDTH
    SCREEN_HEIGHT = config.SCREEN_HEIGHT
    INITIAL_IMAGE = config.INITIAL_IMAGE
    PAUSE_IMAGE = config.PAUSE_IMAGE
    
    def __init__(self):
        self.screen = pygame.display.set_mode((PauseScreen.SCREEN_WIDTH, PauseScreen.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
       
        
    def run(self):

        self.running = True

        while self.running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_v:  # Pressione 'p' novamente para despausar
                        self.running = False
            
            self.screen.blit(PauseScreen.PAUSE_IMAGE, (0, 0))

            pygame.display.update()
            self.clock.tick(30)
