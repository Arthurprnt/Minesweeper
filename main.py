import pygame

from grid import Grid, Case
from func import collide, showtext
from imports import *
pygame.init()

length = 9

while running:

    screen.blit(background.image, background.pos)

    if stats == 0:
        screen.blit(logo.image, logo.pos)
        if collide(start_game["target"], pygame.mouse.get_pos()):
            screen.blit(start_game["target"].image, start_game["target"].pos)
        else:
            screen.blit(start_game["away"].image, start_game["away"].pos)
        showtext(screen, f"Grid size: {length}", "assets/DIN_Bold.ttf", 75, (screen_x//2 - 240, screen_y//2 + 190), (255, 255, 255), False)
        screen.blit(triangle_up.image, triangle_up.pos)
        screen.blit(triangle_down.image, triangle_down.pos)
    elif stats == 1:
        for x in range(length):
            for y in range(length):
                screen.blit(grille.grid[x][y].image, grille.grid[x][y].pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                if stats == 0:
                    if collide(start_game["target"], event.pos):
                        stats = 1
                        grille = Grid(length)
                    elif collide(triangle_up, event.pos) and length < 30:
                        if pygame.key.get_pressed()[pygame.K_LCTRL] and length < 28:
                            length += 3
                        else:
                            length += 1
                    elif collide(triangle_down, event.pos) and length >= 10:
                        if pygame.key.get_pressed()[pygame.K_LCTRL] and length >= 12:
                            length -= 3
                        else:
                            length -= 1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()