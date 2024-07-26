# Example file showing a circle moving on screen
import pygame
import math
from tools import Direction

# pygame setup
pygame.init()
clock = pygame.time.Clock()
running = True

screen = pygame.display.set_mode((1400, 800))
dt = 0

snake_head = pygame.Rect(screen.get_width() / 2, screen.get_height() / 2, 20, 20)
snake_direction = Direction.NONE

counter = 0

while running:
    counter += 1
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#1f1f1f")

    # Draw Player
    pygame.draw.rect(screen, "red", snake_head)

    # Event on pressed WSAD keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        snake_direction = Direction.UP
    elif keys[pygame.K_s]:
        snake_direction = Direction.DOWN
    elif keys[pygame.K_a]:
        snake_direction = Direction.LEFT
    elif keys[pygame.K_d]:
        snake_direction = Direction.RIGHT

    # Move snake
    if counter >= 15:
        counter = 0
        match snake_direction:
            case Direction.UP:
                snake_head.y -= 20
            case Direction.DOWN:
                snake_head.y += 20
            case Direction.LEFT:
                snake_head.x -= 20
            case Direction.RIGHT:
                snake_head.x += 20

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()