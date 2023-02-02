import webbrowser, os
from grid import Grid, findotheremptycase, eventpostocoord
from func import collide, showtext, updatestats1, checkwin, addscore
from imports import *
pygame.init()

length = 12

"""
Stats:
0 = Home screen
1 = Game
2 = Finised
"""

while running:

    screen.blit(background.image, background.pos)

    if debug:
        showtext(screen, str(pygame.mouse.get_pos()), "assets/DIN_Bold.ttf", 30, (40, screen_y-50), (255, 255, 255), "topleft")
        print(stats)

    if stats == 0:
        screen.blit(logo.image, logo.pos)
        if collide(start_game["target"], pygame.mouse.get_pos()):
            screen.blit(start_game["target"].image, start_game["target"].pos)
        else:
            screen.blit(start_game["away"].image, start_game["away"].pos)
        showtext(screen, f"Grid size: {length}", "assets/DIN_Bold.ttf", 75, (screen_x//2 - 240, screen_y//2 + 190), (255, 255, 255), "midleft")
        screen.blit(triangle_up.image, triangle_up.pos)
        screen.blit(triangle_down.image, triangle_down.pos)
    elif stats == 1:
        if first_bomb_clicked:
            time[1] += 1/60
            if time[1] >= 60:
                time[0] += 1
                time[1] = 0
            if checkwin(length, grille):
                txt_win = "You won !"
                # Send stats to the .csv file
                stats = 2
                addscore(nickname, time, length)
        updatestats1(screen, cases_flagged, grille, length, color_per_number, flag, time)
    elif stats == 2:
        updatestats1(screen, cases_flagged, grille, length, color_per_number, flag, time)
        showtext(screen, txt_win, "assets/DIN_Bold.ttf", 72, (screen_x - 50, 30), (255, 255, 255), "topright")
        if collide(restart_game["target"], pygame.mouse.get_pos()):
            screen.blit(restart_game["target"].image, restart_game["target"].pos)
        else:
            screen.blit(restart_game["away"].image, restart_game["away"].pos)
        if collide(ranking["target"], pygame.mouse.get_pos()):
            screen.blit(ranking["target"].image, ranking["target"].pos)
        else:
            screen.blit(ranking["away"].image, ranking["away"].pos)
        for x in range(length):
            for y in range(length):
                case = grille.grid[x][y]
                if case.bombed:
                    screen.blit(bomb, case.pyimage.pos)

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
                                    time = [0, 0]
                                if not(case.flaged):
                                    case.pyimage.image = pygame.image.load("assets/open_case.png")
                                    if case.bombed:
                                        txt_win = "Game over"
                                        stats = 2
                                    else:
                                        if case.value == 0:
                                            findotheremptycase(eventpostocoord(event.pos, coords), grille.grid)
                                        else:
                                            case.opened = True
                                    len_cases_opened = 0
                                    len_bombs_flaged = 0
                            if collide(case.pyimage, event.pos):
                                case.checkcomplete(grille, nickname, time, length)
                elif stats == 2:
                    if collide(restart_game["target"], event.pos):
                        del grille
                        first_bomb_clicked = False
                        cases_flagged = 0
                        stats = 0
                    if collide(ranking["target"], event.pos):
                        webbrowser.open_new_tab(os.path.abspath("leaderboard/index.html"))
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