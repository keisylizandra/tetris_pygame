import pygame
import config
import random
import os 

class Board:
    
    HEIGHT_TOP_BAR = config.HEIGHT_TOP_BAR
    SCREEN_WIDTH = config.SCREEN_WIDTH
    SCREEN_HEIGHT = config.SCREEN_HEIGHT
    BAR_COLOR = config.BAR_COLOR

    def __init__(self, screen, image):
        self.image = image
        self.score =  0
        self.screen = screen

       
        # Define a fonte e o texto
        font_path = config.FONT_PATH
        self.font = pygame.font.Font(font_path , 25)
        self.text = self.font.render(f'Score: {self.score}', True, (0, 0, 0))  # Black text

        # Desenha o texto no centro da barra
        self.text_rect = self.text.get_rect(center=(screen.get_width() / 2, Board.HEIGHT_TOP_BAR / 2))

        self.matriz = []
        for row in range(int(Board.SCREEN_HEIGHT / self.image.get_height())):
            self.matriz.append([])
            for col in range(int(Board.SCREEN_WIDTH / self.image.get_width())):
                self.matriz[row].append(0)
        


    def draw(self, screen):
         # Cria um retângulo no topo da tela
        pygame.draw.rect(self.screen, Board.BAR_COLOR, pygame.Rect(0, 0, Board.SCREEN_WIDTH, Board.HEIGHT_TOP_BAR))

        self.text = self.font.render(f'Score: {self.score}', True, (0, 0, 0))  # Black text

        screen.blit(self.text, self.text_rect)

        for row in range(len(self.matriz)):
            for col in range(len(self.matriz[row])):
                if self.matriz[row][col] == 1:
                    pos_x = self.image.get_width() * col
                    pos_y = self.image.get_height() * row
                    screen.blit(self.image, (pos_x , pos_y))


    def eraseLine(self, screen):
        erasedLine = -1
        self.points = 0

        # Itera sobre cada linha da matriz de cima para baixo
        for j in range(2):
            for row in reversed(range(len(self.matriz))):
                # Verifica se a linha está completa (não contém 0)
                if 0 not in self.matriz[row]:
                    # Set all values in the row to 0
                    self.points += 100
                    self.matriz[row] = [0] * len(self.matriz[row])
                    erasedLine = row

        matriz_aux = []
        y = 0

        if erasedLine != -1:
            fist_Line_With_1 = -1
            for row in range(erasedLine):
                if 1 in self.matriz[row]:
                    if fist_Line_With_1 == -1:
                        fist_Line_With_1 = row

                    matriz_aux.append(self.matriz[row])
                    self.matriz[row] = [0] * len(self.matriz[row])

            y = fist_Line_With_1 * config.IMAGE_LIST[0].get_height()
        

        if(self.points != 0):
            self.score += self.points
            config.point_sound.play()
            self.increaseSpeed()

        return y, matriz_aux


    def increaseSpeed(self):
        if self.score == 500 or self.score == 1000:
            config.SPEED += 1
        else:
            config.SPEED = config.SPEED


                            
    
  