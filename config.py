import os
import pygame


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
HEIGHT_TOP_BAR = 75

BAR_COLOR = (255,255,255)

IMAGE_LIST = [pygame.image.load(os.path.join("assets", "piscadinha.png")), pygame.image.load(os.path.join("assets", "bichinha.png")), pygame.image.load(os.path.join("assets", "apaixonado.png")), pygame.image.load(os.path.join("assets", "zeRuela.png")), pygame.image.load(os.path.join("assets", "medroso.png"))]
SPEED = 2
FONT_PATH = os.path.join("assets", "Honk-Regular.ttf")

TICK = 30
pygame.mixer.init()
BACKGROUND_IMAGE = pygame.image.load(os.path.join("assets","background.png"))
INITIAL_IMAGE = pygame.image.load(os.path.join("assets","Tetris.png"))
GAMEOVER_IMAGE = pygame.image.load(os.path.join("assets","gameOver.png"))
POINT_SOUND_PATH = os.path.join("assets", "collect-ring-15982.mp3")
GAMEOVER_SOUND_PATH = os.path.join("assets", "videogame-death-sound-43894 (1).mp3")
point_sound = pygame.mixer.Sound(POINT_SOUND_PATH)
gameOver_sound = pygame.mixer.Sound(GAMEOVER_SOUND_PATH)

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
                [1, 1],
                [1, 1],
                [1, 1]
            ],

            [
                [0, 1, 1],
                [1, 1, 0]
            ]
        ]