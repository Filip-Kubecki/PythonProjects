# Example file showing a circle moving on screen
import pygame
import math
from Snake import Snake
from tools import Direction

# Pygame setup
pygame.init()
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
running = True

# Snake object setup
snake = Snake(screen.get_width() / 2, screen.get_height() / 2)

# Apple rectangle


# Game variables
dt = 0
counter = 0


# Main loop of game -------------------------------------------------------------------------
while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#1f1f1f")

    # Draw snake object
    snake.draw_snake(screen)

    # Event on pressed WSAD keys
    keys = pygame.key.get_pressed()
    snake.key_event(keys)

    # Update state of snake: position and directions of segments
    if counter >= 15:
        counter = 0
        if keys[pygame.K_p]:
          snake.add_segment()
        snake.update()

    # Update everything on screen
    pygame.display.flip()

    counter += 1

    # limits FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()