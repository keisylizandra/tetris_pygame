import pygame
import random
import os 
import config

#create a block class
class Block:
    IMAGE_LIST = config.IMAGE_LIST
    SCREEN_WIDTH = config.SCREEN_WIDTH
    SCREEN_HEIGHT = config.SCREEN_HEIGHT


    def __init__(self, shape, x, y):
        self.SPEED = config.SPEED
        self.image = random.choice(Block.IMAGE_LIST)
        self.shape = shape
        self.x = x
        self.y = y
        self.collision = False


    def draw(self, screen, board):
        for row in range(len(self.shape)):
            for col in range(len(self.shape[row])):
                if self.shape[row][col] == 1:
                    pos_x = self.x + self.image.get_width() * col
                    pos_y = self.y + self.image.get_height() * row
                    self.checkCollision(pos_y, board)
                    screen.blit(self.image, (pos_x , (pos_y)))


    def moveDown(self):
        if not self.collision:
            self.y += self.SPEED
            

    def checkCollision(self, pos_y, board):
        if (self.image.get_height() + pos_y) >= Block.SCREEN_HEIGHT or self.isOcuppied(board):
            self.collision = True

    
    def moveLeftOrRight(self, direction, board):
        if direction == "right" and self.x < (Block.SCREEN_WIDTH - self.image.get_width() * len(self.shape[0])) and self.sideCollision(board, direction):
            self.x += self.image.get_width()

        elif direction == "left" and self.x > 0 and self.sideCollision(board, direction):
            self.x -= self.image.get_width()

    
    def checkPositionAtBoard(self, board):
        for row in range(len(self.shape)):
            for column in range(len(self.shape[row])):
                if self.shape[row][column] == 1: 
                    pos_x = self.x + (column + 1) * self.image.get_width()
                    pos_y = self.y + (row + 1) * self.image.get_height()

                    coordinateRow = pos_y // self.image.get_height() - 1 
                    coordinateCol = pos_x // self.image.get_width() - 1

                    board.matriz[coordinateRow][coordinateCol] = 1

                 
                       
    def isOcuppied(self, board):
        for row in range(len(self.shape)):
            for column in range(len(self.shape[row])):
                if self.shape[row][column] == 1: 
                    pos_x = self.x + (column + 1) * self.image.get_width()
                    pos_y = self.y + (row + 1) * self.image.get_height()

                    coordinateRow = pos_y // self.image.get_height() - 1 
                    coordinateCol = pos_x // self.image.get_width() - 1

                    if 0 <= coordinateRow + 1 < len(board.matriz) and 0 <= coordinateCol < len(board.matriz[0]):
                        if board.matriz[coordinateRow + 1][coordinateCol] == 1:
                            return True  # A posição está ocupada

        return False  # A posição não está ocupada

    

    def sideCollision(self, board, direction):

        for row in range(len(self.shape)):
            for column in range(len(self.shape[row])):
                if self.shape[row][column] == 1: 
                    pos_x = self.x + (column + 1) * self.image.get_width()
                    pos_y = self.y + (row + 1) * self.image.get_height()

                    coordinateRow = pos_y // self.image.get_height() - 1 
                    coordinateCol = pos_x // self.image.get_width() - 1

                    if ((coordinateCol + 1) < len(board.matriz[0]) and board.matriz[coordinateRow][coordinateCol + 1] == 1) and direction == 'right':
                        return False  # The position is occupied
                    
                    if ((coordinateCol - 1) >= 0 and board.matriz[coordinateRow][coordinateCol - 1] == 1) and direction == 'left':
                        return False

        return True  # The position is not occupied 
    

    def rotate(self, shape):
        rotated_shape = [list(x) for x in zip(*shape[::-1])]

        if len(rotated_shape) == len(shape[0]) and len(rotated_shape[0]) == len(shape) and self.x + self.image.get_width() * len(rotated_shape) >= Block.SCREEN_WIDTH:
            self.x -= (len(rotated_shape[0]) - len(shape[0])) * self.image.get_width()
            return rotated_shape
        else:
            return rotated_shape
    


    def keepMoving(self, board):
        shapes = [] 
        for row in range(len(self.shape)):
            for column in range(len(self.shape[row])):
                if self.shape[row][column] == 1: 
                    pos_x = self.x + (column + 1) * self.image.get_width()
                    pos_y = self.y + (row + 1) * self.image.get_height()

                    coordinateRow = pos_y // self.image.get_height() - 1 
                    coordinateCol = pos_x // self.image.get_width() - 1

                    if 0 <= coordinateRow + 1 < len(board.matriz) and 0 <= coordinateCol < len(board.matriz[0]):
                        if board.matriz[coordinateRow + 1][coordinateCol] == 1:

                            return True  # A posição está ocupada

        return False  # A posição não está ocupada
  




  