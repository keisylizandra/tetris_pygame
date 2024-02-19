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
        linhaApagada = -1
        self.points = 0
        # Itera sobre cada linha da matriz de cima para baixo
        for j in range(2):
            for row in reversed(range(len(self.matriz))):
                # Verifica se a linha está completa (não contém 0)
                if 0 not in self.matriz[row]:
                    del self.matriz[row]
                    linhaApagada = row
        

        if(linhaApagada != -1):
            matriz_aux = []
            primeira_linha_com_1 = -1
            for row in range(linhaApagada):
                if 1 in self.matriz[row]:
                    if(primeira_linha_com_1 == -1):
                        primeira_linha_com_1 = row
                    matriz_aux.append(self.matriz[row])


            for i in range(len(matriz_aux)):
                print(matriz_aux[i])

            y =  primeira_linha_com_1 * config.IMAGE_LIST[0].get_height()





            
        
                    
                 


            
        if(self.points != 0):
            self.score += self.points
            config.point_sound.play()
            self.increaseSpeed()
        
        print(f'linha apagada: {linhaApagada}')
        

    def increaseSpeed(self):
        if self.score == 500 or self.score >= 1000:
            config.SPEED += 1
        else:
            config.SPEED = config.SPEED


                            
    
  