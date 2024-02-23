import os
import pygame


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
HEIGHT_TOP_BAR = 75
NEXT_KEY_TIME = 0

BAR_COLOR = (255,255,255)

IMAGE_LIST = [pygame.image.load(os.path.join("assets/imgs", "piscadinha.png")), pygame.image.load(os.path.join("assets/imgs", "bichinha.png")), pygame.image.load(os.path.join("assets/imgs", "apaixonado.png")), pygame.image.load(os.path.join("assets/imgs", "zeRuela.png")), pygame.image.load(os.path.join("assets/imgs", "medroso.png"))]
SPEED = 3
FONT_PATH = os.path.join("assets/fonts", "Honk-Regular.ttf")

TICK = 30
pygame.mixer.init()
BACKGROUND_IMAGE = pygame.image.load(os.path.join("assets/imgs","background.png"))
INITIAL_IMAGE = pygame.image.load(os.path.join("assets/imgs","Tetris.png"))
GAMEOVER_IMAGE = pygame.image.load(os.path.join("assets/imgs","gameOver.png"))
PAUSE_IMAGE = pygame.image.load(os.path.join("assets/imgs","pauseScreen.png"))
POINT_SOUND_PATH = os.path.join("assets/sounds", "collect-ring-15982.mp3")
GAMEOVER_SOUND_PATH = os.path.join("assets/sounds", "videogame-death-sound-43894 (1).mp3")
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