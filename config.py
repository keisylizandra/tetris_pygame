import os
import pygame


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
HEIGHT_TOP_BAR = 75
BAR_COLOR = (0, 0, 0)
IMAGE_LIST = [pygame.image.load(os.path.join("assets", "piscadinha.png")), pygame.image.load(os.path.join("assets", "bichinha.png")), pygame.image.load(os.path.join("assets", "apaixonado.png")), pygame.image.load(os.path.join("assets", "zeRuela.png")), pygame.image.load(os.path.join("assets", "medroso.png"))]
SPEED = 4
FONT_PATH = os.path.join("assets", "Honk-Regular.ttf")

TICK = 30
pygame.mixer.init()
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
                [1, 1],
                [1, 1],
                [1, 1]
            ],

           
        ]