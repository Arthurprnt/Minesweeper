import pygame
from func import pygameimage

running = True
stats = 0
screen = pygame.display.set_mode()
screen_x, screen_y = screen.get_size()
pygame.display.set_caption('Minesweeper')
pygame.display.set_icon(pygame.image.load('assets/icon.png'))
clock = pygame.time.Clock()

background = pygameimage(pygame.image.load('assets/background.png'), (screen_x // 2 - 2560 // 2, screen_y // 2 - 1440 // 2))
logo = pygameimage(pygame.transform.scale(pygame.image.load('assets/logo.png'), (1500, 525)), (screen_x // 2 - 1500 // 2, screen_y // 60))
start_game = {
    "away": pygameimage(pygame.transform.scale(pygame.image.load("assets/start_game.png"), (737, 132)), (screen_x // 2 - 737 // 2, screen_y // 2)),
    "target": pygameimage(pygame.transform.scale(pygame.image.load("assets/start_game_target.png"), (737, 132)), (screen_x // 2 - 737 // 2, screen_y // 2))
}