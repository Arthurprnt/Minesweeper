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