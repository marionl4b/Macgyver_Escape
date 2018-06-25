import pygame
import random
from settings import *
from main import *


def load_img(filename):
    img = pygame.image.load(path.join(IMG_DIR, filename)).convert_alpha()
    return img


def load_snd(filename):
    pass


def draw_text(text, font, size, color, x, y):
    font = pygame.font.Font(font, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    SCREEN.blit(text_surface, text_rect)


class Labyrinth:
    def __init__(self):
        self.screen = SCREEN
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

        # store position of road and walls tiles
        for row, tiles in enumerate(self.grid):
            for col, tile in enumerate(tiles):
                if tile == ROAD:  # add walls by cols and rows
                    self.road(col, row)
                    self.road_pos.append(self.road_rect)
                if tile == WALL:  # add walls by cols and rows
                    self.wall(col, row)
                    self.walls_pos.append(self.wall_rect)

        # load objects randomly on road tile, MacGyver and the Gate Keeper
        self.objects = [self.object() for i in range(3)]
        i = -1
        for self.obj in self.objects:
            i += 1
            self.obj['img'] = load_img(OBJ_IMG_LIST[i])
        self.macgyver()
        self.gate_keeper()

    def show_map(self):

        """ init the map for display in GameWrapper """
        # show walls and roads loaded by row and col
        for row, tiles in enumerate(self.grid):
            for col, tile in enumerate(tiles):
                if tile == WALL:
                    self.wall(col, row)
                    self.screen.blit(self.wall_image, self.wall_rect)
                if tile == ROAD:
                    self.road(col, row)
                    self.screen.blit(self.road_image, self.road_rect)

        # show the 3 collectibles objects and MacGyver and the Gate Keeper
        for self.obj in self.objects:
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
        # self.wall_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        # self.wall_image.fill(BLACK)
        self.wall_image = load_img('wall.png')
        self.wall_rect = self.wall_image.get_rect()
        self.wall_rect.x = x * TILE_SIZE
        self.wall_rect.y = y * TILE_SIZE
        self.wall_rect = (self.wall_rect.x, self.wall_rect.y)

    def road(self, x, y):

        """ init tile walls for the map """
        # self.wall_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        # self.wall_image.fill(BLACK)
        self.road_image = load_img('road.png')
        self.road_rect = self.road_image.get_rect()
        self.road_rect.x = x * TILE_SIZE
        self.road_rect.y = y * TILE_SIZE
        self.road_rect = (self.road_rect.x, self.road_rect.y)

    def object(self):

        """ init the objects with a dictionary """
        self.obj_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.obj_image.fill(VIOLET)
        # self.obj_image = load_img(OBJ_IMG_LIST[0])
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
        # self.gk_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        # self.gk_image.fill(RED)
        self.gk_image = load_img('murdoc.png')
        self.gk_rect = self.gk_image.get_rect()
        self.gk_rect.x = 12 * TILE_SIZE
        self.gk_rect.y = 11 * TILE_SIZE

    def macgyver(self):

        """ init MacGyver """
        # self.mg_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        # self.mg_image.fill(BLUE)
        self.mg_image = load_img('macgyver.png')
        self.mg_rect = self.mg_image.get_rect()
        self.mg_rect.x = 0 * TILE_SIZE
        self.mg_rect.y = 2 * TILE_SIZE

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
                self.obj['img'] = load_img('road.png')
                print("Un objet à été ramassé")
            if self.obj['taken'] is False:
                self.game_over = True
            else:
                self.game_over = False

    def move(self, key):

        """ Move MacGyver if all is clear and declare which object is collected """
        new_x, new_y = self.get_new_coords(key)
        self.check_objects(new_x, new_y)
        if self.check_coords(new_x, new_y) is True:
            self.mg_rect.x = new_x
            self.mg_rect.y = new_y
            self.end_game()

    def end_game(self):

        """ check MacGyver position to detect victory """
        if self.mg_rect.x == self.gk_rect.x and self.mg_rect.y == self.gk_rect.y:
            if self.game_over is True:
                print("Game Over!")
                self.objects = [self.object() for i in range(3)]
                i = -1
                for self.obj in self.objects:
                    i += 1
                    self.obj['img'] = load_img(OBJ_IMG_LIST[i])
                self.macgyver()
            else:
                print("Gagné!")
                self.objects = [self.object() for i in range(3)]
                i = -1
                for self.obj in self.objects:
                    i += 1
                    self.obj['img'] = load_img(OBJ_IMG_LIST[i])
                self.macgyver()









