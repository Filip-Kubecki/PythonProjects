import pygame
from resources import Style
from config import *
from GameMenu import GameMenu

# Pygame setup
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Snake")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True

delta_time = 0  # time in seconds since last frame - used for limiting FPS

# Shit to test
menu = GameMenu(WINDOW_WIDTH, WINDOW_HEIGHT)

temp_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
temp_surf.fill(Style.MOSSE_GREEN)
temp_surf.set_alpha(20)

# Main loop of game -----------------------------------------------------------
while running:
    # pygame.QUIT event means the user clicked X to close window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    menu.display(screen)

    # Update everything on screen
    pygame.display.flip()

    # limits FPS to 120
    delta_time = clock.tick(120) / 1000

pygame.quit()
