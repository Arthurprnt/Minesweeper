import random

import pygame.image

from func import pygameimage
from imports import screen_x, screen_y, case_size

class Grid():

    def __init__(self, size, oo_coords):

        self.size = size

        self.grid = []
        coords = oo_coords
        for y in range(self.size):
            self.grid.append([])
            if y%2 == 0:
                color_image = 0
            else:
                color_image = 1
            for x in range(self.size):
                if color_image == 0:
                    self.grid[y].append(Case(pygame.image.load("assets/dark_case.png"), (coords[0], coords[1])))
                    color_image = 1
                elif color_image == 1:
                    self.grid[y].append(Case(pygame.image.load("assets/light_case.png"), (coords[0], coords[1])))
                    color_image = 0
                coords[0] += case_size
            coords[0] = screen_x // 2 - size * case_size // 2
            coords[1] += case_size

    def addbombs(self, mousecoords, coords):
        # Find the first coord that have been clicked
        nb_x, nb_y = eventpostocoord(mousecoords, coords)

        # Make that the first case clicked value is 0
        self.coords_bomb = []
        fake_boombs = []
        for y in range(-1, 2):
            for x in range(-1, 2):
                fake_boombs.append((nb_y+y, nb_x+x))

        for _ in range(self.size ** 2 // 8):
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            while (y, x) in self.coords_bomb or (y, x) in fake_boombs:
                x = random.randint(0, self.size - 1)
                y = random.randint(0, self.size - 1)
            self.grid[y][x].bombed = True
            self.coords_bomb.append((y, x))

        for y in range(self.size):
            for x in range(self.size):
                if self.grid[y][x].bombed is False:
                    # Every case which not bombed is analysed
                    bombs = 0
                    for y_case in range(-1, 2):
                        for x_case in range(-1, 2):
                            if 0 <= x + x_case <= self.size - 1 and 0 <= y + y_case <= self.size - 1 and (nb_x, nb_y) != (nb_x+x, nb_y+y):
                                if self.grid[y + y_case][x + x_case].bombed:
                                    bombs += 1
                    self.grid[y][x].value = bombs


class Case():

    def __init__(self, image, pos):
        self.pyimage = pygameimage(image, pos)
        self.value = 9
        self.opened = False
        self.bombed = False
        self.flaged = False

def eventpostocoord(mousecoord, oo_coords):
    x, y = mousecoord
    nb_x = 0
    nb_y = 0
    while x > oo_coords[0]:
        x -= 45
        nb_x += 1
    while y > oo_coords[1]:
        y -= 45
        nb_y += 1
    return nb_x-1, nb_y-1

def findotheremptycase(mousecoord, coords, grid):
    nb_x, nb_y = coords
    if 0 <= nb_x < len(grid[0]) and 0 <= nb_y < len(grid[0]) and grid[nb_y][nb_x].value == 0 and grid[nb_y][nb_x].opened is False and grid[nb_y][nb_x].flaged is False:
        grid[nb_y][nb_x].pyimage.image = pygame.image.load("assets/open_case.png")
        grid[nb_y][nb_x].opened = True
        coordtovisit = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        return findotheremptycase(mousecoord, (coords[0]+coordtovisit[0][0], coords[1]+coordtovisit[0][1]), grid), findotheremptycase(mousecoord, (coords[0]+coordtovisit[1][0], coords[1]+coordtovisit[1][1]), grid), findotheremptycase(mousecoord, (coords[0]+coordtovisit[2][0], coords[1]+coordtovisit[2][1]), grid), findotheremptycase(mousecoord, (coords[0]+coordtovisit[3][0], coords[1]+coordtovisit[3][1]), grid)
    elif 0 <= nb_x < len(grid[0]) and 0 <= nb_y < len(grid[0]) and grid[nb_y][nb_x].value != 9 and grid[nb_y][nb_x].flaged is False:
        grid[nb_y][nb_x].pyimage.image = pygame.image.load("assets/open_case.png")
        grid[nb_y][nb_x].opened = True
        return None
    else:
        return None