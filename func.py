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