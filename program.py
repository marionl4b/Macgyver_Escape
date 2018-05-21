#! /usr/bin/env python3
# coding: utf-8

import random
import os
import pickle
import itertools

DIR_PATH = os.path.dirname(os.path.abspath(__file__))  # return api directory
WALL = "X"
ROAD = " "
MACGYVER = "M"
GATE_KEEPER = "G"
OBJECTS = ["1", "2", "3"]


def store_grid():

    """ setup and store random labyrinth grid 15x15 in grid.txt """

    stored_grid = []
    i = 0
    for line in range(15):
        i += 1
        line = [WALL] * 5 + [ROAD] * 10
        while i == 1:
            line[0] = MACGYVER
            break
        random.shuffle(line)
        # line = " ".join(line)+"\n"
        stored_grid += [line]
    with open(os.path.join(DIR_PATH, 'grid.txt'), 'wb') as file:
        mon_pickler = pickle.Pickler(file)
        mon_pickler.dump(stored_grid)
    # return stored_grid


def show_grid():

    """ show the grid stored before """

    with open(os.path.join(DIR_PATH, 'grid.txt'), 'rb') as file:
        mon_depickler = pickle.Unpickler(file)
        show_grid = mon_depickler.load()
    # show_grid = " ".join(show_grid(listes)+"\n"
    return(show_grid)

def player_move():

    """take keyboard action and make MacGyver move on the grid in theory"""
    # new_grid = stored_grid
    key_board = input()
    if key_board == "u":
        #MACGYVER indice -1 move left
        pass
    elif key_board == "i":
        #MACGYVER indice +1 move right
        pass
    elif key_board == "j":
        #MACGYVER indice -15 move up
        pass
    elif key_board == "k":
        #MACGYVER indice +15 move down
        pass
    else:
        #MACGYVER initial indice stay in place
        pass
    #return new grid for stored_grid()


def main():

    """ Merlin : what's you're favorite colour ? Galaad : Blue, no Red, aaaaargh """

    store_grid()
    print(show_grid())


if __name__ == "__main__":
    main()
