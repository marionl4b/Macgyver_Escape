# Macgyver Escape a labyrinth game using pygame
# !/usr/bin/env python3
# coding: utf-8

import pygame
from labyrinth_sprites import *
from settings import *


class GameWrapper:
    """ init the game loop """

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = SCREEN
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.waiting = True

        # init functions of labyrinth
        self.labyrinth = Labyrinth()

        self.start_screen()

    def events(self):
        """ init process input loop """
        while True:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.wating = False
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.labyrinth.move('up')
                    elif event.key == pygame.K_DOWN:
                        self.labyrinth.move('down')
                    elif event.key == pygame.K_LEFT:
                        self.labyrinth.move('left')
                    elif event.key == pygame.K_RIGHT:
                        self.labyrinth.move('right')
            # self.update()
            self.draw()

    # def update(self):
    #     self.game_over_screen()

    def draw(self):
        """ render graphics """

        self.screen.fill(GREEN)
        self.labyrinth.show_map()
        pygame.display.flip()

    def start_screen(self):
        self.screen.fill(BLUE)
        draw_text(TITLE, FONT_BOLD, 24, WHITE, WIDTH/2, HEIGHT / 3)
        draw_text("Make the Gate Keeper sleep to escape from the maze ", FONT, 18, WHITE, WIDTH/2, 220)
        draw_text("Press Arrow to move", FONT, 18, WHITE, WIDTH / 2, 280)
        draw_text("Press Any key to start", FONT, 18, WHITE, WIDTH / 2, 300)
        pygame.display.flip()
        self.restart()

    def game_over_screen(self):
        win = self.labyrinth.end_game()
        if not win:
            self.screen.fill(RED)
            draw_text("GAME OVER !", FONT_BOLD, 24, WHITE, WIDTH / 2, HEIGHT / 3)
            draw_text("Press Any key to restart", FONT, 18, WHITE, WIDTH / 2, 300)
            pygame.display.flip()
            self.restart()
        else:
            self.screen.fill(GREEN)
            draw_text("GAGNÉ !", FONT_BOLD, 24, WHITE, WIDTH / 2, HEIGHT / 3)
            draw_text("Press Any key to restart", FONT, 18, WHITE, WIDTH / 2, 300)
            pygame.display.flip()
            self.restart()

    def restart(self):
        while self.waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.waiting = False
                if event.type == pygame.KEYUP:
                    self.waiting = False
                    self.events()


def main():
    """ execute pygame game """

    game = GameWrapper()
    game.start_screen()
    pygame.quit()


if __name__ == '__main__':
    main()

