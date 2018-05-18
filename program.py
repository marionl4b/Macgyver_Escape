#! /usr/bin/env python3
# coding: utf-8

import random

WALL = "X"
ROAD = " "
MAC_GYVER = "M"
GATE_KEEPER = "G"
OBJECTS = ["1", "2", "3"]

def grid():
    """ setup random labyrinth grid 15x15 """
    grid = " "
    for line in range(15):
        line = [WALL] * 7 + [ROAD] * 8
        random.shuffle(line)
        line = " ".join(line)+"\n"
        grid += line
    return grid

print(grid())
