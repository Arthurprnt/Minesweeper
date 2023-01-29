import pygame

class pygameimage():

    def __init__(self, image, pos):
        self.image = image
        self.pos = pos
        self.size = image.get_size()

    def gethitbox(self):
        return (self.pos[0], self.pos[0] + self.size[0], self.pos[1], self.pos[1] + self.size[1])

def collide(image, mouse):
    """
    Check if the mouse cursor collide with an image.
    """
    hitbox = image.gethitbox()
    return hitbox[0] <= mouse[0] <= hitbox[1] and hitbox[2] <= mouse[1] <= hitbox[3]

def showtext(screen, text, font, size, pos, color, align):
    """
    Show text on the screen
    """
    final_font = pygame.font.Font(font, size)
    text_shown = final_font.render(text, True, color)
    text_rect = text_shown.get_rect()
    if align.lower() == "center":
        text_rect.center = pos
    elif align.lower() == "midleft":
        text_rect.midleft = pos
    elif align.lower() == "midright":
        text_rect.midright = pos
    elif align.lower() == "topleft":
        text_rect.topleft = pos
    elif align.lower() == "topright":
        text_rect.topright = pos
    elif align.lower() == "bottomleft":
        text_rect.bottomleft = pos
    else:
        text_rect.bottomright = pos
    screen.blit(text_shown, text_rect)

def updatestats1(screen, cases_flagged, grille, length, color_per_number, flag):
    showtext(screen, f"{cases_flagged}/{grille.size ** 2 // 8}", "assets/DIN_Bold.ttf", 80, (50, 80), (255, 255, 255),
             "midleft")
    for x in range(length):
        for y in range(length):
            case = grille.grid[x][y]
            screen.blit(case.pyimage.image, case.pyimage.pos)
            if case.opened:
                if case.bombed:
                    pass
                elif case.value > 0:
                    showtext(screen, f"{case.value}", "assets/DIN_Bold.ttf", 30, (case.pyimage.pos[0] + 45 // 2, case.pyimage.pos[1] + 45 // 2), color_per_number[str(case.value)], "center")
            if case.flaged:
                screen.blit(flag, case.pyimage.pos)
