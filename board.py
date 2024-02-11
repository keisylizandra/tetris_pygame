import pygame
import os 

class Board:
    IMAGE = pygame.image.load(os.path.join("assets", "block.png"))
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 600

    def __init__(self):
        self.matriz = []
        for row in range(int(Board.SCREEN_HEIGHT / Board.IMAGE.get_height())):
            self.matriz.append([])
            for col in range(int(Board.SCREEN_WIDTH / Board.IMAGE.get_width())):
                self.matriz[row].append(0)


    def draw(self, screen):
        for row in range(len(self.matriz)):
            for col in range(len(self.matriz[row])):
                if self.matriz[row][col] == 1:
                    pos_x = Board.IMAGE.get_width() * col
                    pos_y = Board.IMAGE.get_height() * row
                    screen.blit(Board.IMAGE, (pos_x , pos_y))