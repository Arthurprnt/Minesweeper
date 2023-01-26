from grid import Grid, Case
from imports import *
pygame.init()

running = True
stats = 0
screen = pygame.display.set_mode()
screen_x, screen_y = screen.get_size()
pygame.display.set_caption('Minesweeper')
clock = pygame.time.Clock()

length = 12

grille = Grid(length)

liste_test = [[0 for _ in range(length)] for _ in range(length)]
for x in range(length):
    for y in range(length):
        liste_test[x][y] = grille.grid[x][y].value
for rangee in liste_test:
    print(rangee)
print(f"Il y a {len(grille.coords_bomb)} bombes.")

while running:

    screen.blit(background, (screen_x // 2 - background.get_size()[0] // 2, screen_y // 2 - background.get_size()[1] // 2))

    if stats == 0:
        screen.blit(logo, (screen_x // 2 - logo.get_size()[0] // 2, screen_y // 60))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()