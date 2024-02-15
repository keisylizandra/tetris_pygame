import pygame
import os 

class Board:
    IMAGE = pygame.image.load(os.path.join("assets", "block.png"))
    HEIGHT_TOP_BAR = IMAGE.get_height()
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 600
    BAR_COLOR = (0, 0, 0)

    def __init__(self, screen):
        self.score =  0
        self.screen = screen
       
        # Define a fonte e o texto
        self.font = pygame.font.Font(None, 15)
        self.text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))  # White text

        # Desenha o texto no centro da barra
        self.text_rect = self.text.get_rect(center=(screen.get_width() / 2, Board.HEIGHT_TOP_BAR / 2))

        self.matriz = []
        for row in range(int(Board.SCREEN_HEIGHT / Board.IMAGE.get_height())):
            self.matriz.append([])
            for col in range(int(Board.SCREEN_WIDTH / Board.IMAGE.get_width())):
                self.matriz[row].append(0)

        


    def draw(self, screen):
         # Cria um retângulo no topo da tela
        pygame.draw.rect(self.screen, Board.BAR_COLOR, pygame.Rect(0, 0, Board.SCREEN_WIDTH, Board.HEIGHT_TOP_BAR))

        self.text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))  # White text
        
        screen.blit(self.text, self.text_rect)

        for row in range(len(self.matriz)):
            for col in range(len(self.matriz[row])):
                if self.matriz[row][col] == 1:
                    pos_x = Board.IMAGE.get_width() * col
                    pos_y = Board.IMAGE.get_height() * row
                    screen.blit(Board.IMAGE, (pos_x , pos_y))


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
        self.score += self.points
        print(self.score)

                            
    
  