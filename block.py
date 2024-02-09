import os
import pygame 

# criar um block

class Block:
    screen_width = 500
    screen_height = 600
    #IMAGE =  pygame.image.load(os.path.join('assets','block.png')) 


    def __init__(self,shape):
        self.shape = shape

    def draw(self,screen):
        for row in range(len(self.shape)):
            for column in range(len(self.shape[row])):
                if self.shape[row][column] == 1:
                    pass
                    #screen.blit(Block.IMAGE,(Block.screen_width/2,Block.screen_height/2))

