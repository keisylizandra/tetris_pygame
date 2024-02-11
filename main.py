import pygame
from block import Block

# Initialize the game
pygame.init()
screen_width = 500
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

shape = [ [1, 1, 1],
          [1, 0, 1] ]

block = Block(shape, 0, 0)

while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                block.moveLeftOrRight("right")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                block.moveLeftOrRight("left")


    # fill the screen with white
    screen.fill(("white"))
    block.draw(screen)
    block.move()

    # update the display
    pygame.display.flip()

    # wait for 1/60th of a second
    clock.tick(60)

pygame.quit()
