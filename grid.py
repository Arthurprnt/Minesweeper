import random

class Grid():

    def __init__(self, size):

        self.size = size
        self.grid = [[Case() for _ in range(size)] for _ in range(size)]
        self.coords_bomb = []

        for _ in range(self.size ** 2 // 8):

            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)

            while (x, y) in self.coords_bomb:
                x = random.randint(0, self.size - 1)
                y = random.randint(0, self.size - 1)

            self.grid[x][y].bombed = True
            self.coords_bomb.append((x, y))

        for x in range(self.size):
            for y in range(self.size):
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

    def __init__(self):
        self.value = 9
        self.bombed = False