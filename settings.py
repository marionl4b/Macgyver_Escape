import pygame
from os import path

pygame.init()


def load_img(filename):
    img = pygame.image.load(path.join(IMG_DIR, filename)).convert_alpha()
    return img


def load_snd(filename):
    snd = pygame.mixer.Sound(path.join(SND_DIR, filename))
    return snd


def load_music(filename):
    music = pygame.mixer.music.load(path.join(SND_DIR, filename))
    return music


def draw_text(text, font, size, color, x, y):
    font = pygame.font.Font(font, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    SCREEN.blit(text_surface, text_rect)


# PATH DIRECTORY
DIR_NAME = path.dirname('__FILE__')
ASSETS_DIR = path.join(DIR_NAME, 'assets')
IMG_DIR = path.join(ASSETS_DIR, 'img')
FONT_DIR = path.join(ASSETS_DIR, 'fonts')
SND_DIR = path.join(ASSETS_DIR, 'sounds')

# Window
WIDTH = 480
HEIGHT = 480
FPS = 30
TITLE = "MAcGyver Escape"
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
RUNNING = True

# Fonts
FONT = path.join(FONT_DIR, 'Comic Sans MS.ttf')
FONT_BOLD = path.join(FONT_DIR, 'Comic Sans MS Bold.ttf')

# Rainbow colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
VIOLET = (105, 60, 132)
BLUE = (55, 169, 204)
GREEN = (89, 188, 106)
YELLOW = (255, 223, 0)
ORANGE = (245, 130, 51)
RED = (198, 29, 38)

# Map
TILE_SIZE = 32
WALL = 'X'
ROAD = '.'

# Objects
OBJ_IMG_LIST = ['tube.png', 'ether.png', 'aiguille.png']