import pygame
import random
from block import Block
from board import Board
from startScreen import StartScreen

# Initialize the game
pygame.init()
screen_width = 500
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

shapes = [
            [
            [1],
            [1],
            [1],
            ],

            [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            ]
        ]

startScreen = StartScreen()
startScreen.run()
block = Block(random.choice(shapes), 0, 0)
board = Board()


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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

    # update the display
    pygame.display.flip()

    # wait for 1/60th of a second
    clock.tick(30)

pygame.quit()
