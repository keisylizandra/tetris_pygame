import os
import pygame


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
HEIGHT_TOP_BAR = 75
BAR_COLOR = (0, 0, 0)
IMAGE_LIST = [pygame.image.load(os.path.join("assets", "piscadinha.png")), pygame.image.load(os.path.join("assets", "bichinha.png")), pygame.image.load(os.path.join("assets", "apaixonado.png")), pygame.image.load(os.path.join("assets", "zeRuela.png")), pygame.image.load(os.path.join("assets", "medroso.png"))]
SPEED = 2
FONT_PATH = os.path.join("assets", "Honk-Regular.ttf")

SHAPES = [
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
                [0, 1],
                [0, 1],
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