import pygame
from block import Block


pygame.init()

screen_width = 500
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()


block_shapes = [
    [
        [1],
        [1],
        [1],
    ],
    [
        [1,1,1],
        [1,0,0],
        [1,0,0]
    ],
]

blockShape = [
        [1],
        [1],
        [1],
    ]

#block = Block(blockShape)


running = True
while running:
    clock.tick(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
     


    screen.fill((255, 255, 255))

    pygame.display.flip()

pygame.quit()
