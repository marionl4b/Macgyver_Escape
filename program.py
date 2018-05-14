#! /usr/bin/env python3
# coding: utf-8

import random

##################################################
#################### GRID SETUP ##################
##################################################

wall = "X"
road = " "
macGyver = "M"
gateKeeper = "G"
objects = ["1", "2", "3"]

def grid():
    grid = " "
    for line in range(15):
        line = [wall] * 7 + [road] * 8
        random.shuffle(line)
        line = " ".join(line)+"\n"
        grid += line
    return grid

print(grid())
