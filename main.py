import pygame
import os
import random
from block import Block
from board import Board
from startScreen import StartScreen
from gameOverScreen import GameOverScreen

# Initialize the game
pygame.init()
screen_width = 500
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
images = [pygame.image.load(os.path.join("assets", "piscadinha.png")), pygame.image.load(os.path.join("assets", "bichinha.png")), pygame.image.load(os.path.join("assets", "apaixonado.png")), pygame.image.load(os.path.join("assets", "zeRuela.png")), pygame.image.load(os.path.join("assets", "medroso.png"))] 

shapes = [
            [
                [1],
                [1],
                [1],
            ],

            [
                [1, 1],
                [1, 1],    
            ],

            [
                [0, 1, 0],
                [1, 1, 1],
            ],

            [
                [1, 1],
                [1, 0]
            ],

            [
                [1, 0],
                [1, 0],
                [1, 1],
            ],

            [
                [1, 1, 1],
                [1, 0, 1]
            ],

            [
                [1, 0],
                [1, 0],
                [1, 1]
            ],

            [
                [1, 1],
                [1, 1],
                [1, 1]
            ],

            [
                [0, 1, 1],
                [1, 1, 0]
            ]
        ]

startScreen = StartScreen()
startScreen.run()
block = Block(random.choice(shapes), 0, 0)
board = Board(screen, random.choice(images))


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                block.shape = block.rotate(block.shape)

    keys = pygame.key.get_pressed()  # get the state of all keyboard keys
    if keys[pygame.K_RIGHT]:  # if the right arrow key is pressed
        block.moveLeftOrRight("right", board)
    if keys[pygame.K_LEFT]:  # if the left arrow key is pressed
        block.moveLeftOrRight("left", board)
    if keys[pygame.K_DOWN]:
        block.moveDown()

    # fill the screen with white
    screen.fill(("white"))
    block.draw(screen, board)
    block.moveDown()
    board.draw(screen)   

    if block.collision:
        block.checkPositionAtBoard(board)
        board.eraseLine(screen)
        block = Block(random.choice(shapes), 0, 0)

        if 1 in board.matriz[0]:
            gameOver = GameOverScreen(board.score)
            running = False
            gameOver.run()


    # update the display
    pygame.display.flip()

    # wait for 1/60th of a second
    clock.tick(30)

pygame.quit()
