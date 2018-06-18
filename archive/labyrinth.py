#! /usr/bin/env python3
# coding: utf-8

import random

WALL = "X"
ROAD = " "
MACGYVER = "M"
GATE_KEEPER = "G"
DIRECTIONS = ("z", "q", "s", "d")


class Labyrinth:
    def __init__(self):
        self.grid = []
        self.mg_x = 0
        self.mg_y = 2
        self.gk_x = 0
        self.gk_y = 0
        self.object = {}
        self.objects = []
        self.game_over = False

        self.load_grid()
        self.show_grid()
        self.play_game()

    def object_constructor(self, name):
        self.object = {
            'name': name,
            'x': random.randint(0, 14),
            'y': random.randint(0, 14),
            'taken': False
        }
        return self.object

    def load_grid(self):

        """ load the grid, MacGyver, the Gate Keeper and the objects positioned"""
        with open('grid.txt', 'r') as file:
            for line in file:
                line = list(line)
                line.pop(15)
                if len(line) > 0:
                    self.grid.append(line)

            self.grid[self.mg_x][self.mg_y] = MACGYVER
            self.grid[self.gk_x][self.gk_x] = GATE_KEEPER

            self.objects = [self.object_constructor(str(i+1)) for i in range(3)]
            for self.object in self.objects:
                self.grid[self.object['x']][self.object['y']] = self.object['name']

    def show_grid(self):

        """ show the grid loaded before """
        for line in self.grid:
            print("".join(line))

    def get_new_coords(self, direction):

        """ get new MacGyver position (x, y) depending on key event """
        x = self.mg_x
        y = self.mg_y

        if direction == "z":
            x -= 1
        elif direction == "q":
            y -= 1
        elif direction == "s":
            x += 1
        elif direction == "d":
            y += 1

        return x, y

    def check_coords(self, x, y):

        """ check clear passage before moving MacGyver depending on direction into the grid """
        if 0 <= x <= 14 and 0 <= y <= 14 and self.grid[x][y] != WALL:
            return True
        else:
            return False

    def check_objects(self, x, y):

        """ check if MacGyver is collecting objects """
        for self.object in self.objects:
            if self.object['x'] == x and self.object['y'] == y:
                self.object['taken'] = True
                return True
            if self.object['taken'] is False:
                self.game_over = True
            else:
                self.game_over = False

    def player_move(self, direction):

        """ Move MacGyver if all is clear and declare which object is collected """
        new_x, new_y = self.get_new_coords(direction)
        if self.check_objects(new_x, new_y) is True:
            print("L'objet {} à été ramassé".format(self.object['name']))
        if self.check_coords(new_x, new_y) is True:
            self.grid[self.mg_x][self.mg_y] = ROAD
            self.grid[new_x][new_y] = MACGYVER
            self.mg_x = new_x
            self.mg_y = new_y
        self.end_game()

    def end_game(self):

        """ check MacGyver position to detect victory """
        if self.mg_x == self.gk_x and self.mg_y == self.gk_y:
            if self.game_over is True:
                print("Game Over!")
            else:
                print("Gagné!")
        else:
            self.show_grid()

    def play_game(self):

        """ event loop which take keyboard action and make MacGyver move inside the grid """
        while True:
            invite = input("Z,Q,S,D :")
            direction = str(invite).lower()
            if direction in DIRECTIONS:
                self.player_move(direction)


def main():

    """ Time to play """
    Labyrinth()


if __name__ == "__main__":
    main()
