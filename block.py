import pygame
import os 

#create a block class
class Block:
    IMAGE = pygame.image.load(os.path.join("assets", "block.png"))
    SPEED = 2
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 600


    def __init__(self, shape, x, y):
        self.shape = shape
        self.x = x
        self.y = y
        self.collision = False


    def draw(self, screen):
        for row in range(len(self.shape)):
            for col in range(len(self.shape[row])):
                if self.shape[row][col] == 1:
                    pos_x = self.x + Block.IMAGE.get_width() * col
                    pos_y = self.y + Block.IMAGE.get_height() * row
                    self.checkCollision(pos_y)
                    screen.blit(Block.IMAGE, (pos_x , pos_y))


    def moveDown(self):
        if not self.collision:
            self.y += Block.SPEED
            

    def checkCollision(self, pos_y):
        if (Block.IMAGE.get_height() + pos_y) >= Block.SCREEN_HEIGHT:
            self.collision = True

    
    def moveLeftOrRight(self, direction):
        if direction == "right" and self.x < (Block.SCREEN_WIDTH - Block.IMAGE.get_width() * len(self.shape[0])):
            self.x += Block.IMAGE.get_width()

        elif direction == "left" and self.x > 0:
            self.x -= Block.IMAGE.get_width()

    
    def checkPositionAtBoard(self,board):
         for row in range(len(self.shape)):
            for column in range(len(self.shape[row])):
                if self.shape[row][column] == 1: 

                    pos_x = self.x + (column + 1) * Block.IMAGE.get_width()
                    pos_y = self.y + (row + 1) * Block.IMAGE.get_height()

                    coordinateRow = pos_y // Block.IMAGE.get_height() - 1
                    coordinateCol = pos_x // Block.IMAGE.get_width() - 1 

                    board.matriz[coordinateRow][coordinateCol] = 1