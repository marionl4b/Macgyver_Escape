# Macgyver Escape a labyrinth game using pygame
# !/usr/bin/env python3
# coding: utf-8

import pygame
from settings import *
from labyrinth_sprites import *


class GameWrapper:
    """ init the game loop """

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

        self.grid = []

        # init classes and sprites of labyrinth_sprites.py
        self.player = Player()
        self.gk = GateKeeper()
        self.obj = Objects()

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player, self.gk)

        self.load_map()

    def load_map(self):
        """ load the map file with walls"""

        with open('map.txt', 'r') as file:
            for row in file:
                row = list(row)
                self.grid.append(row)

        # load the walls by cols and rows
        for row, tiles in enumerate(self.grid):
            for col, tile in enumerate(tiles):
                if tile == 'X':
                    t = Wall(col, row)
                    self.all_sprites.add(t)

    def show_grid(self):
        """" show the grid """

        for x in range(0, WIDTH, TILE_SIZE):
            pygame.draw.line(self.screen, WHITE, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE_SIZE):
            pygame.draw.line(self.screen, WHITE, (0, y), (WIDTH, y))

    def events(self):
        """ init process input loop"""

        self.clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.move('up')
                elif event.key == pygame.K_DOWN:
                    self.player.move('down')
                elif event.key == pygame.K_LEFT:
                    self.player.move('left')
                elif event.key == pygame.K_RIGHT:
                    self.player.move('right')

    def update(self):
        """ logic of the game, collisions"""
        pass

    def draw(self):
        """ render graphics"""

        self.screen.fill(GREEN)
        self.all_sprites.draw(self.screen)
        self.show_grid()
        pygame.display.flip()


def main():
    """ execute pygame game """

    # Pygame init
    pygame.init()
    pygame.mixer.init()
    game = GameWrapper()

    # Event loop
    game.running = True
    while game.running:
        game.events()
        game.update()
        game.draw()
    pygame.quit()


if __name__ == '__main__':
    main()

