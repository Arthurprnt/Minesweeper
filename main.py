from grid import Grid, Case
from func import collide
from imports import *
pygame.init()

length = 9

grille = Grid(length)

liste_test = [[0 for _ in range(length)] for _ in range(length)]
for x in range(length):
    for y in range(length):
        liste_test[x][y] = grille.grid[x][y].value
for rangee in liste_test:
    print(rangee)
print(f"Il y a {len(grille.coords_bomb)} bombes.")

while running:

    screen.blit(background.image, background.pos)

    if stats == 0:
        screen.blit(logo.image, logo.pos)
        if collide(start_game["target"], pygame.mouse.get_pos()):
            screen.blit(start_game["target"].image, start_game["target"].pos)
        else:
            screen.blit(start_game["away"].image, start_game["away"].pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()