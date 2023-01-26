import pygame
import random
pygame.init()

running = True
stats = 0
screen = pygame.display.set_mode()
screen_x, screen_y = screen.get_size()
pygame.display.set_caption('Démineur')
clock = pygame.time.Clock()

class Grid():
    
    def __init__(self, size):
        
        self.size = size
        self.grid = [[Case() for _ in range(size)] for _ in range(size)]
        self.coords_bomb = []
        
        for _ in range(self.size+self.size//5):
            
            x = random.randint(0, self.size-1)
            y = random.randint(0, self.size-1)
            
            while (x, y) in self.coords_bomb:
                
                x = random.randint(0, self.size-1)
                y = random.randint(0, self.size-1)
                
            self.grid[x][y].bombed = True
            self.coords_bomb.append((x, y))
        
        for x in range(self.size):
            for y in range(self.size):
                if self.grid[x][y].bombed is False:
                    # Every case which not bombde is analysed
                    bombs = 0
                    for x_case in range(-1, 2):
                        for y_case in range(-1, 2):
                            if x+x_case >= 0 and x+x_case <= self.size-1 and y+y_case >= 0 and y+y_case <= self.size-1 and not(x_case == 0 and y_case == 0):
                                if self.grid[x+x_case][y+y_case].bombed:
                                    bombs += 1
                    self.grid[x][y].value = bombs
        
class Case():
    
    def __init__(self):
        self.value = 9
        self.bombed = False
        
length = int(input("Taille: "))

grille = Grid(length)

liste_test = [[0 for _ in range(length)] for _ in range(length)]
for x in range(length):
    for y in range(length):
        liste_test[x][y] = grille.grid[x][y].value
for rangee in liste_test:
    print(rangee)
print(f"Il y a {len(grille.coords_bomb)} bombes.")

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
    clock.tick(60)

pygame.quit()