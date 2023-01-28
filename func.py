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

def showtext(screen, text, font, size, pos, color, center):
    """
    Show text on the screen
    """
    final_font = pygame.font.Font(font, size)
    text_shown = final_font.render(text, True, color)
    text_rect = text_shown.get_rect()
    if center:
        text_rect.center = pos
    else:
        text_rect.midleft = pos
    screen.blit(text_shown, text_rect)

def eventpostocoord(mousecoord, oo_coords):
    nb_x = 1
    while mousecoord[0] > oo_coords[0]:
        x = x - 45
        nb_x = nb_x + 1
    nb_y = 1
    while mousecoord[1] > oo_coords[1]:
        y = y - 45
        nb_y = nb_y + 1
    return nb_x, nb_y

def findotheremptycase(mousecoord, oo_coords, grid):
    nb_x, nb_y = eventpostocoord(mousecoord, oo_coords)
    if grid[nb_x][nb_y] != 0:
        return
    else:
        for y in range(-1, 2):
            for x in range(-1, 2):
                if 0 <= nb_x+x < len(grid[0]) and 0 <= nb_y+y < len(grid[0]):
                    if grid[nb_x+x][nb_y+y].value == 0:
                        grid[nb_x+x][nb_y+y].pyimage.image = pygame.image.load("assets/open_case.png")
                        grid[nb_x+x][nb_y+y].opened = True
                        return findotheremptycase(mousecoord, (oo_coords[0]+45*(nb_x+x), oo_coords[1]+45*(nb_y+y)))
                    else:
                        return