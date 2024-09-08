import pygame.freetype
import pygame
from config import *
from resources import TexturesSrc, Style
from GameWrapper import GameWrapper
from GameMenu import GameMenu


# Pygame setup
pygame.init()
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Game wrapper
game = GameWrapper(WINDOW_WIDTH, WINDOW_HEIGHT)

# Game main menu
main_menu = GameMenu(
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    play_method=(game.toggle_visible),
    exit_method=(game.stop)
)

# Game variables
delta_time = 0  # time in seconds since last frame - used for limiting FPS
counter = 0

# Main loop of game -----------------------------------------------------------
while game.running:
    # pygame.QUIT event means the user clicked X to close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                counter = 0
                game.set_pause_game(not game.get_pause_game())

            if game.get_pause_game() and event.key == pygame.K_TAB:
                game.pause_screen.next_focused()

            if game.get_game_over() and event.key == pygame.K_TAB:
                game.game_over_screen.focus()

    # game.game_cycle()
    # screen.blit(game, (0, 0))
    if not game.get_visible():
        main_menu.display(
            screen
        )
    else:
        game.game_cycle()
        screen.blit(game, (0, 0))

    # Update everything on screen
    pygame.display.flip()

    # limits FPS to 120
    delta_time = clock.tick(120) / 1000

pygame.quit()
