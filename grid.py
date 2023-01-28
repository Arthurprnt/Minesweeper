import random

import pygame.image

from func import pygameimage
from imports import screen_x, screen_y, case_size

class Grid():

    def __init__(self, size, coords):

        self.size = size

        self.grid = []
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

        # Find the first coord that have been clicked
        nb_x, nb_y = eventpostocoord(pygame.mouse.get_pos(), coords)

        # Make that the first case clicked value is 0
        self.coords_bomb = []
        for y in range(-1, 2):
            for x in range(-1, 2):
                self.coords_bomb.append((nb_x+x, nb_y+y))

        for _ in range(self.size ** 2 // 8):
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            while (x, y) in self.coords_bomb:
                x = random.randint(0, self.size - 1)
                y = random.randint(0, self.size - 1)
            self.grid[y][x].bombed = True
            self.coords_bomb.append((x, y))

        for y in range(self.size):
            for x in range(self.size):
                if self.grid[x][y].bombed is False:
                    # Every case which not bombde is analysed
                    bombs = 0
                    for x_case in range(-1, 2):
                        for y_case in range(-1, 2):
                            if 0 <= x + x_case <= self.size - 1 and 0 <= y + y_case <= self.size - 1 and not (x_case == 0 and y_case == 0):
                                if self.grid[x + x_case][y + y_case].bombed:
                                    bombs += 1
                    self.grid[x][y].value = bombs


class Case():

    def __init__(self, image, pos):
        self.pyimage = pygameimage(image, pos)
        self.value = 9
        self.opened = False
        self.bombed = False

def eventpostocoord(mousecoord, oo_coords):
    x, y = mousecoord
    x += 10
    y += 10
    nb_x = 1
    while x > oo_coords[0]:
        x = x - 45
        nb_x = nb_x + 1
    nb_y = 1
    while y > oo_coords[1]:
        y = y - 45
        nb_y = nb_y + 1
    print((nb_x-1, nb_y-1))
    return nb_x-1, nb_y-1

def findotheremptycase(mousecoord, oo_coords, grid):
    nb_x, nb_y = eventpostocoord(mousecoord, oo_coords)
    if grid[nb_x][nb_y] != 0:
        return
    else:
        for y in range(-1, 2):
            for x in range(-1, 2):
                if 0 <= nb_x+x < len(grid[0]) and 0 <= nb_y+y < len(grid[0]):
                    if grid[nb_x+x][nb_y+y].value == 0:
                        grid[nb_x+x][nb_y+y].pyimage.image = pygame.image.load("assets/open_case.png")
                        grid[nb_x+x][nb_y+y].opened = True
                        return findotheremptycase(mousecoord, (oo_coords[0]+45*(nb_x+x), oo_coords[1]+45*(nb_y+y)))
                    else:
                        return