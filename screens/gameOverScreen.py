import pygame
from entities.board import Board 
import configs.config as config
import dataBase.firebase_database as firebase_database
import game


#create a block class
class GameOverScreen:
    SCREEN_WIDTH = config.SCREEN_WIDTH
    SCREEN_HEIGHT = config.SCREEN_HEIGHT
    GAMEOVER_IMAGE = config.GAMEOVER_IMAGE

    def __init__(self, score):
        
        config.gameOver_sound.play()
        font_path = config.FONT_PATH
        self.screen = pygame.display.set_mode((GameOverScreen.SCREEN_WIDTH, GameOverScreen.SCREEN_HEIGHT))
        self.score = score
        self.clock = pygame.time.Clock()
        self.text_score = pygame.font.Font(font_path, 30).render(f'Score: {self.score}', True, (0,0,0))
        self.text_best_score = pygame.font.Font(font_path, 30).render(f'Best score: {firebase_database.getHighestScore()}', True, (0,0,0))
        self.text_rect = self.text_score.get_rect(center=(GameOverScreen.SCREEN_WIDTH // 2, GameOverScreen.SCREEN_HEIGHT // 2 + 80))
        self.text_rect_best_score = self.text_best_score.get_rect(center=(GameOverScreen.SCREEN_WIDTH // 2, (GameOverScreen.SCREEN_HEIGHT // 2 + 110)))
        
    def run(self, board):

        self.running = True
        while self.running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        board.resetBoard()
                        game.main()
                        self.running = False
                        
           

            # fill the screen with white
            self.screen.blit(GameOverScreen.GAMEOVER_IMAGE, (0, 0))
            self.screen.blit(self.text_score, (self.text_rect))
            self.screen.blit(self.text_best_score, (self.text_rect_best_score))

            # update the display
            pygame.display.flip()

            # wait for 1/60th of a second
            self.clock.tick(30)
        