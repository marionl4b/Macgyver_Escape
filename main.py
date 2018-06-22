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

        # init functions of labyrinth
        self.labyrinth = Labyrinth()

    def events(self):
        """ init process input loop """

        self.clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.labyrinth.move('up')
                elif event.key == pygame.K_DOWN:
                    self.labyrinth.move('down')
                elif event.key == pygame.K_LEFT:
                    self.labyrinth.move('left')
                elif event.key == pygame.K_RIGHT:
                    self.labyrinth.move('right')

    def update(self):
        """ logic of the game, collisions """
        pass

    def draw(self):
        """ render graphics """

        self.screen.fill(GREEN)
        self.labyrinth.show_map()

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

