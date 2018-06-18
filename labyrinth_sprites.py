import pygame
import random
from settings import *
from main import *


class Wall(pygame.sprite.Sprite):
    """ init tile walls for the map """

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE


class Objects(pygame.sprite.Sprite):
    """ init randomly the objects """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.object = {}
        self.objects = [self.object_constructor(str(i + 1)) for i in range(3)]
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(VIOLET)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH - (TILE_SIZE * self.object['x'])
        self.rect.y = HEIGHT - (TILE_SIZE * self.object['y'])

    def object_constructor(self, name):
        self.object = {
            'name': name,
            'x': random.randint(0, 14),
            'y': random.randint(0, 14),
            'taken': False
        }
        return self.object


class GateKeeper(pygame.sprite.Sprite):
    """ init the Gate Keeper """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH - (TILE_SIZE*6)
        self.rect.y = HEIGHT - (TILE_SIZE*8)


class Player(pygame.sprite.Sprite):

    """ init MacGyver """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH/2 - TILE_SIZE/2
        self.rect.y = HEIGHT/2 - TILE_SIZE/2

    def get_new_coords(self, key):

        """ get new MacGyver position (x, y) depending on key event """
        x = self.rect.x
        y = self.rect.y
        if key == 'up':
            self.rect.y -= TILE_SIZE
        elif key == 'down':
            self.rect.y += TILE_SIZE
        elif key == 'left':
            self.rect.x -= TILE_SIZE
        elif key == 'right':
            self.rect.x += TILE_SIZE

        return x, y

    def check_coords(self, x, y):

        """ check clear passage before moving MacGyver depending on direction into the map """
        # grid = GameWrapper.load_map()
        # if 0 <= x < WIDTH and 0 <= y < HEIGHT and grid[x][y] != WALL:
        if 0 <= x < WIDTH and 0 <= y < HEIGHT:
            return True
        else:
            return False

    def move(self, key):

        """ Move MacGyver if all is clear and declare which object is collected """
        x = self.rect.x
        y = self.rect.y
        self.get_new_coords(key)
        new_x, new_y = self.get_new_coords(key)
        if self.check_coords(new_x, new_y) is True:
            self.rect.x = new_x
            self.rect.y = new_y
        # else:
        #     self.rect.x = x
        #     self.rect.y = y

