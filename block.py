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


    def move(self):
        if not self.collision:
            self.y += Block.SPEED
            

    def checkCollision(self, pos_y):
        if (Block.IMAGE.get_height() + pos_y) >= Block.SCREEN_HEIGHT:
            self.collision = True

    
    def moveLeftOrRight(self, direction):
        if direction == "right":
            self.x += Block.IMAGE.get_width()
        elif direction == "left":
            self.x -= Block.IMAGE.get_width()