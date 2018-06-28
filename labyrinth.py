import random
from settings import *


class Labyrinth:
    def __init__(self):
        self.screen = SCREEN
        self.grid = []
        self.walls_pos = []
        self.road_pos = []
        self.objects = []
        self.inventory = 0
        self.game_over = False

        self.load_map()
        self.set_new_map()

    def load_map(self):
        """ load the map file and store wall and road positions"""

        # open and read the map
        with open('map.txt', 'r') as file:
            for row in file:
                row = list(row)
                self.grid.append(row)

        # store position of road and walls tiles
        for row, tiles in enumerate(self.grid):
            for col, tile in enumerate(tiles):
                if tile == ROAD:  # add walls by cols and rows
                    road_image, road_rect = self.set_road(col, row, 'road.png')
                    self.road_pos.append(road_rect)
                if tile == WALL:  # add walls by cols and rows
                    wall_image, wall_rect = self.set_wall(col, row, 'wall.png')
                    self.walls_pos.append(wall_rect)

    def set_new_map(self):

        """ load 3 objects randomly on road tile then load MacGyver and the Gate Keeper """
        self.objects = [self.set_object() for i in range(3)]
        i = -1
        for obj in self.objects:
            i += 1
            obj['img'] = load_img(OBJ_IMG_LIST[i])
        self.set_macgyver(0, 2, 'macgyver.png')
        self.set_gate_keeper(14, 11, 'murdoc.png')
        self.inventory = 0

    def show_map(self):

        """ set the map images for display in GameWrapper """
        # show walls and roads loaded by row and col
        for row, tiles in enumerate(self.grid):
            for col, tile in enumerate(tiles):
                if tile == WALL:
                    wall_image, wall_rect = self.set_wall(col, row, 'wall.png')
                    self.screen.blit(wall_image, wall_rect)
                if tile == ROAD:
                    road_image, road_rect = self.set_road(col, row, 'road.png')
                    self.screen.blit(road_image, road_rect)

        # show the 3 collectibles objects MacGyver and the Gate Keeper
        for obj in self.objects:
            self.screen.blit(obj['img'], obj['rect'])
        self.screen.blit(self.mg_image, self.mg_rect)
        self.screen.blit(self.gk_image, self.gk_rect)

        # add grid lines
        for x in range(0, WIDTH, TILE_SIZE):
            pygame.draw.line(self.screen, WHITE, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE_SIZE):
            pygame.draw.line(self.screen, WHITE, (0, y), (WIDTH, y))

    def set_wall(self, x, y, filename):

        """ set tile walls for the map """
        wall_image = load_img(filename)
        wall_rect = wall_image.get_rect()
        wall_rect.x = x * TILE_SIZE
        wall_rect.y = y * TILE_SIZE
        wall_rect = (wall_rect.x, wall_rect.y)
        return wall_image, wall_rect

    def set_road(self, x, y, filename):

        """ set tile walls for the map """
        road_image = load_img(filename)
        road_rect = road_image.get_rect()
        road_rect.x = x * TILE_SIZE
        road_rect.y = y * TILE_SIZE
        road_rect = (road_rect.x, road_rect.y)
        return road_image, road_rect

    def set_object(self):

        """ construct the objects with a dictionary """
        obj_image = load_img(OBJ_IMG_LIST[0])
        obj_rect = obj_image.get_rect()
        obj_rect.x = TILE_SIZE * random.randint(0, 14)
        obj_rect.y = TILE_SIZE * random.randint(0, 14)
        obj_rect = random.choice(self.road_pos)

        obj = {
            'img': obj_image,
            'rect': obj_rect
        }
        return obj

    def set_gate_keeper(self, x, y, filename):

        """ set the Gate Keeper """
        self.gk_image = load_img(filename)
        self.gk_rect = self.gk_image.get_rect()
        self.gk_rect.x = x * TILE_SIZE
        self.gk_rect.y = y * TILE_SIZE

    def set_macgyver(self, x, y, filename):

        """ set MacGyver """
        self.mg_image = load_img(filename)
        self.mg_rect = self.mg_image.get_rect()
        self.mg_rect.x = x * TILE_SIZE
        self.mg_rect.y = y * TILE_SIZE

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
        for obj in self.objects:
            if obj['rect'] == test_pos:
                snd_effect = load_snd('SUCCESS PICKUP.ogg')
                snd_effect.play()
                self.inventory += 1
                self.objects.remove(dict(obj))
                # print(self.inventory)
                # print("Un objet à été ramassé")
            if not self.inventory == 3:
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
                snd_effect = load_snd('NEGATIVE Failure.ogg')
                snd_effect.play()
            else:
                snd_effect = load_snd('EXPLOSION.ogg')
                snd_effect.play()
            return True
        else:
            return False


