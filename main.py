import pygame
import os
import random
import config
from block import Block
from board import Board
from startScreen import StartScreen
from gameOverScreen import GameOverScreen
from pauseScreen import PauseScreen
import firebase_database

# Initialize the game
pygame.init()
screen_width = config.SCREEN_WIDTH
screen_height = config.SCREEN_HEIGHT
background_image = config.BACKGROUND_IMAGE
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
images = config.IMAGE_LIST

shapes = config.SHAPES

startScreen = StartScreen()
startScreen.run()
pauseScreen = PauseScreen()
block = Block(random.choice(shapes), (screen_width//2), 4)
board = Board(screen, random.choice(images))
tick = config.TICK
next_key_time = config.NEXT_KEY_TIME


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pauseScreen.run()
            if event.key == pygame.K_UP and (block.y + images[0].get_width() * len(block.shape) < screen_height - images[0].get_width()):
                if event.key == pygame.K_UP:
                    block.shape = block.rotate(block.shape)

    keys = pygame.key.get_pressed()  # get the state of all keyboard keys
    if keys[pygame.K_RIGHT] and current_time >= next_key_time:  # if the right arrow key is pressed
        block.moveLeftOrRight("right", board)
        next_key_time = current_time + 100
    if keys[pygame.K_LEFT] and current_time >= next_key_time:  # if the left arrow key is pressed
        block.moveLeftOrRight("left", board)
        next_key_time = current_time + 100
    if keys[pygame.K_DOWN]:
        block.moveDown()

    # fill the screen with white
    current_time = pygame.time.get_ticks()
    screen.blit(background_image, (0, 0))
    block.draw(screen, board)
    block.moveDown()
    board.draw(screen)   


    if block.collision:
        block.checkPositionAtBoard(board)

        y,matriz_aux = board.eraseLine(screen)

        if(matriz_aux != []):
            block = Block(matriz_aux, 0, y)    
        else:
            block = Block(random.choice(shapes), (screen_width//2), 0)
            if 1 in board.matriz[3]:
                gameOver = GameOverScreen(board.score)
                running = False
                firebase_database.addScoreToFireBase({'Score': board.score})
                gameOver.run()


    # update the display
    pygame.display.flip()

    # wait for 1/60th of a second
    clock.tick(tick)

pygame.quit()
