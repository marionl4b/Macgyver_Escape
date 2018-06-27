# Macgyver Escape a labyrinth game using pygame
# !/usr/bin/env python3
# coding: utf-8

import pygame
from labyrinth import *
from settings import *


class GameWrapper:
    """ init the game loop """

    def __init__(self):
        self.screen = SCREEN
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.waiting = True
        self.game_over = False

        # init functions of labyrinth
        self.labyrinth = Labyrinth()

    def game_loop(self):
        while self.running:
            self.clock.tick(FPS)
            while self.game_over:
                self.game_over_screen()
            self.events()
            self.update()
            self.draw()

    def events(self):
        """ init process input loop """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
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

    def update(self):
        """ logic """

        if self.labyrinth.end_game():
            self.game_over = True

    def draw(self):
        """ render graphics """

        self.screen.fill(GREEN)
        self.labyrinth.show_map()
        pygame.display.flip()

    def start_screen(self):
        load_music('8-Bit Tunes MacGyver Theme.mp3')
        pygame.mixer.music.play(loops=-1)
        start_bg = load_img('start_bg.png')
        start_bg_rect = start_bg.get_rect()
        self.screen.blit(start_bg, start_bg_rect)
        draw_text(TITLE, FONT_BOLD, 24, WHITE, WIDTH/2, 300)
        draw_text("Make the Gate Keeper sleep to escape from the maze ", FONT, 18, WHITE,  WIDTH / 2, 360)
        draw_text("Press Arrows to move", FONT, 18, WHITE, WIDTH / 2, 400)
        draw_text("Press Any key to start", FONT, 18, WHITE, WIDTH / 2, 420)
        pygame.display.flip()
        while self.waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.waiting = False
                    self.running = False
                elif event.type == pygame.KEYUP:
                    self.waiting = False
                    self.game_loop()

    def game_over_screen(self):

        if self.labyrinth.game_over:
            self.screen.fill(ORANGE)
            go_bg = load_img('go_bg.png')
            go_bg_rect = go_bg.get_rect()
            self.screen.blit(go_bg, go_bg_rect)
            self.screen.blit(go_bg, go_bg_rect)
            draw_text("GAME OVER!", FONT_BOLD, 32, WHITE, WIDTH / 2, HEIGHT / 3)
            draw_text("Press 'y' to restart and 'n' to quit", FONT, 18, WHITE, WIDTH / 2, 210)
        else:
            self.screen.fill(GREEN)
            win_bg = load_img('win_bg.png')
            win_bg_rect = win_bg.get_rect()
            self.screen.blit(win_bg, win_bg_rect)
            self.screen.blit(win_bg, win_bg_rect)
            draw_text("YOU WIN!", FONT_BOLD, 32, WHITE, WIDTH / 2, HEIGHT / 3)
            draw_text("Press 'y' to restart and 'n' to quit", FONT, 18, WHITE, WIDTH / 2, 210)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = False
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                self.game_over = False
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                self.game_over = False
                self.labyrinth.set_new_map()


def main():
    """ execute pygame game """
    pygame.init()
    pygame.mixer.init()
    game = GameWrapper()
    game.start_screen()
    game.game_loop()
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()

