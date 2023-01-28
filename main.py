import pygame

from grid import Grid, findotheremptycase, eventpostocoord
from func import collide, showtext
from imports import *
pygame.init()

length = 9

"""
Stats:
0 = Home screen
1 = Game
2 = Finised
"""

while running:

    screen.blit(background.image, background.pos)

    if debug:
        showtext(screen, str(pygame.mouse.get_pos()), "assets/DIN_Bold.ttf", 30, (40, screen_y-50), (255, 255, 255), False)

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
        showtext(screen, f"{cases_flagged}/{grille.size ** 2 // 8}", "assets/DIN_Bold.ttf", 80, (50, 80), (255, 255, 255), False)
        for x in range(length):
            for y in range(length):
                case = grille.grid[x][y]
                screen.blit(case.pyimage.image, case.pyimage.pos)
                if case.opened:
                    if case.bombed:
                        pass
                    elif case.value > 0:
                        showtext(screen, f"{case.value}", "assets/DIN_Bold.ttf", 30, (case.pyimage.pos[0] + 45//2, case.pyimage.pos[1] + 45//2), color_per_number[str(case.value)], True)
                if case.flaged:
                    screen.blit(flag, case.pyimage.pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_F4:
                debug = not (debug)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                if stats == 0:
                    if collide(start_game["target"], event.pos):
                        stats = 1
                        coords = [(screen_x // 2) - ((length * case_size) // 2), (screen_y // 2) - ((length * case_size) // 2)]
                        grille = Grid(length, coords)
                        coords[1] -= length*case_size # If I don't put this the code don't work, idk why x)
                    elif collide(triangle_up, event.pos) and length < 23:
                        if pygame.key.get_pressed()[pygame.K_LCTRL] and length < 21:
                            length += 3
                        else:
                            length += 1
                    elif collide(triangle_down, event.pos) and length >= 10:
                        if pygame.key.get_pressed()[pygame.K_LCTRL] and length >= 12:
                            length -= 3
                        else:
                            length -= 1
                elif stats == 1:
                    for line in grille.grid:
                        for case in line:
                            if not(case.opened) and collide(case.pyimage, event.pos):
                                if first_bomb_clicked is False:
                                    first_bomb_clicked = True
                                    grille.addbombs(event.pos, coords)
                                case.pyimage.image = pygame.image.load("assets/open_case.png")
                                if case.bombed:
                                    stats = 3
                                else:
                                    if case.value == 0:
                                        findotheremptycase(event.pos, eventpostocoord(event.pos, coords), grille.grid)
                                    else:
                                        case.opened = True
            elif event.button == pygame.BUTTON_RIGHT:
                if stats == 1:
                    for line in grille.grid:
                        for case in line:
                            if collide(case.pyimage, event.pos):
                                x, y = eventpostocoord(event.pos, coords)
                                if grille.grid[y][x].opened is False:
                                    if grille.grid[y][x].flaged:
                                        cases_flagged -= 1
                                        grille.grid[y][x].flaged = False
                                    elif cases_flagged < grille.size ** 2 // 8:
                                        cases_flagged += 1
                                        grille.grid[y][x].flaged = True

    pygame.display.flip()
    clock.tick(60)

pygame.quit()