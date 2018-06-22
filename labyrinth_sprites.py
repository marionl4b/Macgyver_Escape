import pygame
import random
from settings import *
from main import *


class Labyrinth:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.grid = []

        self.game_over = False

        self.walls_pos = []
        self.road_pos = []
        self.obj = {}
        self.objects = []
        self.load_map()

    def load_map(self):
        """ load the map file and objects"""

        # open and read the map
        with open('map.txt', 'r') as file:
            for row in file:
                row = list(row)
                self.grid.append(row)

        # store position of road tiles
        for row, tiles in enumerate(self.grid):
            for col, tile in enumerate(tiles):
                if tile == ROAD:  # add walls by cols and rows
                    self.wall(col, row)
                    self.road_pos.append(self.wall_rect)

        # load objects randomly on road tile, MacGyver and the Gate Keeper
        self.objects = [self.object() for i in range(3)]
        self.macgyver()
        self.gate_keeper()

    def show_map(self):

        """ init the map for display in GameWrapper """
        # show walls loaded by row and col
        for row, tiles in enumerate(self.grid):
            for col, tile in enumerate(tiles):
                if tile == WALL:  # add walls by cols and rows
                    self.wall(col, row)
                    self.walls_pos.append(self.wall_rect)
                    self.screen.blit(self.wall_image, self.wall_rect)

        # show the 3 collectibles objects and MacGyver and the Gate Keeper
        for self.obj in self.objects:
            if not self.obj['taken']:
                self.screen.blit(self.obj['img'], self.obj['rect'])
        self.screen.blit(self.mg_image, self.mg_rect)
        self.screen.blit(self.gk_image, self.gk_rect)

        # add grid lines
        for x in range(0, WIDTH, TILE_SIZE):
            pygame.draw.line(self.screen, WHITE, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE_SIZE):
            pygame.draw.line(self.screen, WHITE, (0, y), (WIDTH, y))

    def wall(self, x, y):

        """ init tile walls for the map """
        self.wall_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.wall_image.fill(BLACK)
        self.wall_rect = self.wall_image.get_rect()
        self.wall_rect.x = x * TILE_SIZE
        self.wall_rect.y = y * TILE_SIZE
        self.wall_rect = (self.wall_rect.x, self.wall_rect.y)

    def object(self):

        """ init the objects with a dictionary """
        self.obj_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.obj_image.fill(VIOLET)
        self.obj_rect = self.obj_image.get_rect()
        self.obj_rect.x = TILE_SIZE * random.randint(0, 14)
        self.obj_rect.y = TILE_SIZE * random.randint(0, 14)
        self.obj_rect = random.choice(self.road_pos)

        self.obj = {
            'img': self.obj_image,
            'rect': self.obj_rect,
            'taken': False
        }
        return self.obj

    def gate_keeper(self):

        """ init the Gate Keeper """
        self.gk_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.gk_image.fill(RED)
        self.gk_rect = self.gk_image.get_rect()
        self.gk_rect.x = WIDTH - (TILE_SIZE*6)
        self.gk_rect.y = HEIGHT - (TILE_SIZE*8)

    def macgyver(self):

        """ init MacGyver """
        self.mg_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.mg_image.fill(BLUE)
        self.mg_rect = self.mg_image.get_rect()
        self.mg_rect.x = WIDTH/2 - TILE_SIZE/2
        self.mg_rect.y = HEIGHT/2 - TILE_SIZE/2

    def get_new_coords(self, key):

        """ get new MacGyver position (x, y) depending on key event """
        x = self.mg_rect.x
        y = self.mg_rect.y

        if key == 'up':
            y -= TILE_SIZE
        elif key == 'down':
            y += TILE_SIZE
        elif key == 'left':
            x -= TILE_SIZE
        elif key == 'right':
            x += TILE_SIZE

        return x, y

    def check_coords(self, x, y):

        """ check clear passage before moving MacGyver depending on direction into the map """
        test_pos = (x, y)
        if 0 <= x < WIDTH and 0 <= y < HEIGHT and test_pos not in self.walls_pos:
            return True
        else:
            return False

    def check_objects(self, x, y):

        """ check if MacGyver is collecting objects """
        test_pos = (x, y)
        for self.obj in self.objects:
            if self.obj['rect'] == test_pos:
                self.obj['taken'] = True
                return True
            if self.obj['taken'] is False:
                self.game_over = True
            else:
                self.game_over = False

    def move(self, key):

        """ Move MacGyver if all is clear and declare which object is collected """
        self.get_new_coords(key)
        new_x, new_y = self.get_new_coords(key)
        if self.check_objects(new_x, new_y) is True:
            print("Un objet à été ramassé")
        if self.check_coords(new_x, new_y) is True:
            self.mg_rect.x = new_x
            self.mg_rect.y = new_y
            self.end_game()

    def end_game(self):

        """ check MacGyver position to detect victory """
        if self.mg_rect.x == self.gk_rect.x and self.mg_rect.y == self.gk_rect.y:
            if self.game_over is True:
                # restart
                print("Game Over!")
            else:
                # restart
                print("Gagné!")




