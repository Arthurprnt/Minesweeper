import random

import pygame.image

from func import pygameimage
from imports import screen_x, screen_y

class Grid():

    def __init__(self, size):

        self.size = size

        self.grid = []
        case_size = 45
        coords = [screen_x // 2 - ((size * case_size) // 2), screen_y // 2 - ((size * case_size) // 2)]
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

        self.coords_bomb = []

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

    def __init__(self, image=pygame.image.load("assets/dark_case.png"), pos=(0, 0)):
        self.image = image
        self.pos = pos
        self.value = 9
        self.bombed = False