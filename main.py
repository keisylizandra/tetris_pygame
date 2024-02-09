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
        [1,1,1],
        [1,1,1],
        [1,1,1],
    ]
blockShape2 = [
        [1,1,1],
        [0,1,0],
        [0,1,0],
    ]

block = Block(blockShape,screen_width/2 - 50,0)


running = True
while running:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                block.moveLeftRight('left')
            if event.key == pygame.K_RIGHT:
                block.moveLeftRight('right')
     
    screen.fill((255, 255, 255))

    block.draw(screen)
    if(not block.colision):
        block.moveDown()
    else:
        block = Block(blockShape2,screen_width/2 - 50,0)


    pygame.display.flip()

pygame.quit()
