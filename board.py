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


    # Função para apagar uma linha completa
    def eraseLine(self, screen):
        # Itera sobre cada linha da matriz de cima para baixo
        for row in reversed(range(len(self.matriz))):
            # Verifica se a linha está completa (não contém 0)
            if 0 not in self.matriz[row]:
                # Para cada linha acima da linha completa, copia a linha de cima para a linha de baixo
                for i in range(row, 0, -1):
                    self.matriz[i] = list(self.matriz[i - 1])
                # Define a primeira linha (a linha mais alta) como uma nova linha vazia
                self.matriz[0] = [0 for _ in self.matriz[0]]
                        
                    
