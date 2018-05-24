#! /usr/bin/env python3
# coding: utf-8

import random
import os

DIR_PATH = os.path.dirname(os.path.abspath(__file__))  # return api directory
WALL = "X"
ROAD = " "
MACGYVER = "M"
GATE_KEEPER = "G"
OBJECTS = ["1", "2", "3"]
DIRECTIONS = ("z", "q", "s", "d")


class Labyrinth:
    def __init__(self):
        self.grid = []
        self.mg_pos = 0
        self.gk_pos = 250

        self.init_grid()
        self.load_grid()
        self.show_grid()
        self.player_move()

    def init_grid(self):

        """ setup and store random labyrinth grid 15x15 in grid.txt """
        init_grid = str()
        for line in range(15):
            line = [WALL] * 4 + [ROAD] * 11
            random.shuffle(line)
            line = " ".join(line)+"\n"
            init_grid += line
        with open(os.path.join(DIR_PATH, 'grid.txt'), 'w') as file:
            file.write(init_grid)

    def load_grid(self):

        with open(os.path.join(DIR_PATH, 'grid.txt'), 'r') as file:
            self.grid = list(file.read())
            self.grid[self.mg_pos] = MACGYVER
            self.grid[self.gk_pos] = GATE_KEEPER
        return self.grid

    def show_grid(self):

        """ show the grid loaded before """
        for line in self.grid:
            print(line, end='')

    def player_move(self):

        """take keyboard action and make MacGyver move on the grid"""

        while True:
            direction = input("Déplacez MacGyver dans le Labyrinthe grace aux touches ZQSD:")

            if direction in DIRECTIONS:
                if direction == "z" and self.grid[self.mg_pos - 30] != WALL:
                    self.mg_pos -= 30   # move up
                elif direction == "q" and self.grid[self.mg_pos - 2] != WALL:
                    self.mg_pos -= 2    # move left
                elif direction == "s" and self.grid[self.mg_pos + 30] != WALL:
                    self.mg_pos += 30   # move right
                elif direction == "d" and self.grid[self.mg_pos + 2] != WALL:
                    self.mg_pos += 2    # move down
            if self.mg_pos == self.gk_pos:
                print("Gagné!")
                break
            else:
                pass
            self.load_grid()
            self.show_grid()


def main():

    """ Time to play : Merlin : what's you're favorite colour ? Galaad : Blue, no Red, aaaaargh """

    Labyrinth()


if __name__ == "__main__":
    main()
