import pygame

from grid import Grid, Case, eventpostocoord
from func import collide, showtext, findotheremptycase
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
                case = grille.grid[x][y]
                screen.blit(case.pyimage.image, case.pyimage.pos)
                if case.opened:
                    if case.bombed:
                        pass
                    elif case.value > 0:
                        showtext(screen, f"{case.value}", "assets/DIN_Bold.ttf", 30, (case.pyimage.pos[0] + 45//2, case.pyimage.pos[1] + 45//2), color_per_number[str(case.value)], True)

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
                        coords = [screen_x // 2 - ((length * case_size) // 2), screen_y // 2 - ((length * case_size) // 2)]
                        grille = Grid(length, coords)
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
                            if collide(case.pyimage, event.pos):
                                case.pyimage.image = pygame.image.load("assets/open_case.png")
                                if case.bombed:
                                    stats = 3
                                else:
                                    case.opened = True
                                    if case.value == 0:
                                        pass
                                        findotheremptycase(event.pos, coords, grille.grid)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()