import os
import pygame 

# criar um block

class Block:
    screen_width = 500
    screen_height = 600
    IMAGE =  pygame.image.load(os.path.join('assets','block.png')) 
    VELOCIDADE = 2


    def __init__(self,shape,x,y):
        self.shape = shape
        self.x = x
        self.y = y
        self.colision = False

    def draw(self,screen):
        for row in range(len(self.shape)):
            for column in range(len(self.shape[row])):
                if self.shape[row][column] == 1: 
                    pos_x = self.x + column * Block.IMAGE.get_width()
                    pos_y = self.y + row * Block.IMAGE.get_height()
                    if(pos_y + Block.IMAGE.get_height() >= Block.screen_height): # quando o bloco toca no chão
                        self.colision = True

                    screen.blit(Block.IMAGE,(pos_x,pos_y))


    def moveDown(self):
        self.y += Block.VELOCIDADE

    def moveLeftRight(self,direction):
        if(direction == 'right'):
            self.x += Block.IMAGE.get_width()
        elif(direction == 'left'):
            self.x -= Block.IMAGE.get_width()




