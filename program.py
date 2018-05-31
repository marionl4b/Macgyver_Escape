#! /usr/bin/env python3
# coding: utf-8

import random

WALL = "X"
ROAD = " "
MACGYVER = "M"
GATE_KEEPER = "G"
OBJECTS = ["1", "2", "3"]
DIRECTIONS = ("z", "q", "s", "d")


class Labyrinth:
    def __init__(self):
        self.grid = []
        self.passage = True
        self.mg_x = 0
        self.mg_y = 2
        self.gk_x = 0
        self.gk_y = 0

        self.load_grid()
        self.show_grid()
        self.play_game()

    def load_grid(self):

        """ load the grid, add MacGyver and Gate Keeper positioned"""

        #  have to load objects

        with open('grid.txt', 'r') as file:
            for line in file:
                line = list(line)
                line.pop(15)
                if len(line) > 0:
                    self.grid.append(line)

            self.grid[self.mg_x][self.mg_y] = MACGYVER
            self.grid[self.gk_x][self.gk_x] = GATE_KEEPER

    def show_grid(self):

        """ show the grid loaded before """

        for line in self.grid:
            print("".join(line))

    def check_free_pass(self, direction):

        """ compare direction with walls and grid limits, return clear or blocked passage for player_move()"""

        if direction == "z" and self.grid[self.mg_x - 1][self.mg_y] == WALL or direction == "z" and self.mg_x == 0:
            self.passage = False  # up passage is blocked
        elif direction == "q" and self.grid[self.mg_x][self.mg_y - 1] == WALL or direction == "q" and self.mg_y == 0:
            self.passage = False  # left passage is blocked
        elif direction == "s" and self.grid[self.mg_x + 1][self.mg_y] == WALL or direction == "s" and self.mg_x == 14:
            self.passage = False  # down passage is blocked
        elif direction == "d" and self.grid[self.mg_x][self.mg_y + 1] == WALL or direction == "d" and self.mg_y == 14:
            self.passage = False  # right passage is blocked
        else:
            self.passage = True  # all is clear

    def player_move(self, direction):

        """ check clear passage before moving MacGyver depending on direction into the grid """

        self.check_free_pass(direction)
        if self.passage is True:
            if direction == "z":
                self.grid[self.mg_x][self.mg_y] = ROAD
                self.mg_x -= 1
                self.grid[self.mg_x][self.mg_y] = MACGYVER  # move up
            elif direction == "q":
                self.grid[self.mg_x][self.mg_y] = ROAD
                self.mg_y -= 1
                self.grid[self.mg_x][self.mg_y] = MACGYVER  # move left
            elif direction == "s":
                self.grid[self.mg_x][self.mg_y] = ROAD
                self.mg_x += 1
                self.grid[self.mg_x][self.mg_y] = MACGYVER  # move down
            elif direction == "d":
                self.grid[self.mg_x][self.mg_y] = ROAD
                self.mg_y += 1
                self.grid[self.mg_x][self.mg_y] = MACGYVER  # move right
            else:
                pass
        print(self.mg_x, self.mg_y)
        print(self.gk_x, self.gk_y)
        print(direction)
        print(self.passage)
        self.end_game()

    def end_game(self):

        """ check MacGyver position to detect victory """

        if self.mg_x == self.gk_x and self.mg_y == self.gk_y:
            print("Gagné!")
        else:
            self.show_grid()

    def play_game(self):

        """ take keyboard action and store these in direction variable
        and make MacGyver move inside the grid to find the Gate Keeper """

        while True:
            invite = input("Z,Q,S,D :")
            direction = invite
            if direction in DIRECTIONS:
                self.player_move(direction)


def main():

    """ Time to play """

    Labyrinth()


if __name__ == "__main__":
    main()
