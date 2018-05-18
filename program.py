#! /usr/bin/env python3
# coding: utf-8

import random
import os
#import pickle

DIR_PATH = os.path.dirname(os.path.abspath(__file__))  # return api directory
WALL = "X"
ROAD = " "
MACGYVER = "M"
GATE_KEEPER = "G"
OBJECTS = ["1", "2", "3"]


def store_grid():

    """ setup and store random labyrinth grid 15x15 in grid.txt """

    stored_grid = ' '
    for line in range(15):
        line = [WALL] * 7 + [ROAD] * 8
        random.shuffle(line)
        line = " ".join(line)+"\n"
        stored_grid += line
    with open(os.path.join(DIR_PATH, 'grid.txt'), 'w') as file:
        file.write(stored_grid)


def main():

    """ Merlin : what's you're favorite colour ? Galaad : Blue, no Red, aaaaargh """

    store_grid()


if __name__ == "__main__":
    main()
