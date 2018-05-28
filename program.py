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
        self.grid_up_pos = []
        self.grid_down_pos = []
        self.grid_left_pos = []
        self.grid_right_pos = []
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
            self.grid_up_pos = [i for i in range(0, 28, 2)]
            self.grid_down_pos = [i for i in range(420, len(self.grid), 2)]
            self.grid_left_pos = [i for i in range(0, len(self.grid), 30)]
            self.grid_right_pos = [i for i in range(28, len(self.grid), 30)]
            self.grid[self.mg_pos] = MACGYVER
            self.grid[self.gk_pos] = GATE_KEEPER

        return self.grid_up_pos
        return self.grid_down_pos
        return self.grid_left_pos
        return self.grid_right_pos
        return self.grid

    def show_grid(self):

        """ show the grid loaded before """
        for line in self.grid:
            print(line, end='')

    def player_move(self):

        """take keyboard action and make MacGyver move on the grid"""

        while True:  # while player move
            direction = input("Déplacez MacGyver dans le Labyrinthe grace aux touches ZQSD:")

            if direction in DIRECTIONS:  # test input
                if direction == "z" and self.grid[self.mg_pos - 30] != WALL and self.mg_pos not in self.grid_up_pos:
                    self.mg_pos -= 30   # move up
                elif direction == "q" and self.grid[self.mg_pos - 2] != WALL and self.mg_pos not in self.grid_left_pos:
                    self.mg_pos -= 2    # move left
                elif direction == "s" and self.grid[self.mg_pos + 30] != WALL \
                        and self.mg_pos not in self.grid_down_pos_pos:
                    self.mg_pos += 30   # move right
                elif direction == "d" and self.grid[self.mg_pos + 2] != WALL and self.mg_pos not in self.grid_right_pos:
                    self.mg_pos += 2    # move down
            if self.mg_pos == self.gk_pos:
                print("Gagné!")
                victory = True
                break
            else:
                pass
            self.load_grid()
            self.show_grid()
            print(self.mg_pos)


def main():

    """ Time to play : Merlin : what's you're favorite colour ? Galaad : Blue, no Red, aaaaargh """

    Labyrinth()


if __name__ == "__main__":
    main()
