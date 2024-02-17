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
        self.font = pygame.font.Font(font_path , 18)
        self.text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))  # White text

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

        self.text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))  # White text

        screen.blit(self.text, self.text_rect)

        for row in range(len(self.matriz)):
            for col in range(len(self.matriz[row])):
                if self.matriz[row][col] == 1:
                    pos_x = self.image.get_width() * col
                    pos_y = self.image.get_height() * row
                    screen.blit(self.image, (pos_x , pos_y))


    # Função para apagar uma linha completa
    def eraseLine(self, screen):
        self.points = 0
        # Itera sobre cada linha da matriz de cima para baixo
        for j in range(2):
            for row in reversed(range(len(self.matriz))):
                # Verifica se a linha está completa (não contém 0)
                if 0 not in self.matriz[row]:
                    self.points += 100
                    # Para cada linha acima da linha completa, copia a linha de cima para a linha de baixo
                    for i in range(row, 0, -1):
                        self.matriz[i] = list(self.matriz[i - 1])
                    # Define a primeira linha (a linha mais alta) como uma nova linha vazia
                    self.matriz[0] = [0 for _ in self.matriz[0]]

        if(self.points != 0):
            self.score += self.points
            config.point_sound.play()
            self.increaseSpeed()
    

    def increaseSpeed(self):
        
        if self.score == 200 or self.score >= 400 or self.score >= 600 or self.score >= 800 or self.score >= 1000:
            config.SPEED += 1
        else:
            config.SPEED = config.SPEED


                            
    
  