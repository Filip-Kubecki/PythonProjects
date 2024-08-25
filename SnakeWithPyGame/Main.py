import pygame
import tools
from GameInstance import GameInstance
from PausedGameScreen import PausedGameScreen
from GameOverScreen import GameOverScreen

SCREEN_WIDTH = 850
SCREEN_HEIGHT = 700

# Pygame setup
pygame.init()
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True

# Create Board object
board = GameInstance()

# Pause screen
pause_screen = PausedGameScreen(SCREEN_WIDTH, SCREEN_HEIGHT)

# Pause screen
game_over_screen = GameOverScreen(SCREEN_WIDTH, SCREEN_HEIGHT)

# Game variables
delta_time = 0  # time in seconds since last frame - used for limiting framerate
counter = 0
game_started = False
pause_game = False
game_over = False
gameTick = 10


# Main loop of game -----------------------------------------------------------
while running:
    # pygame.QUIT event means the user clicked X to close window
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                counter = 0
                pause_game = not pause_game
        if event.type == pygame.QUIT:
            running = False

    # Main surface background
    screen.fill("grey")

    # Run one board cycle
    board.run_game_cycle()

    # Taking keyboard input
    keys = pygame.key.get_pressed()

    # Start game when WSAD pressed
    if (keys[pygame.K_w] or
        keys[pygame.K_s] or
        keys[pygame.K_a] or
            keys[pygame.K_d]):
        game_started = True

    # Change pace of the game
    if keys[pygame.K_1]:
        gameTick = 60
    elif keys[pygame.K_2]:
        gameTick = 10
    elif keys[pygame.K_3]:
        gameTick = 5

    # Update state of snake: position and directions of segments
    if counter >= gameTick:
        counter = 0
        if not pause_game and not game_over and game_started:
            board.snake_update()

    # Display game instance surface
    screen.blit(board.screen, (25, 75))

    # Self collision - game over
    if board.snake_collision_game_over():
        screen.blit(
            game_over_screen,
            tools.two_surfaces_centering_offset(screen, game_over_screen))
        game_over_screen.display(screen)
        game_over = True

    # display pause screen
    if pause_game and not game_over:
        screen.blit(
            pause_screen,
            tools.two_surfaces_centering_offset(screen, pause_screen))
        pause_screen.display(screen)

    # Update everything on screen
    pygame.display.flip()

    # Update in game timmer
    counter += 1

    # limits FPS to 60
    delta_time = clock.tick(60) / 1000

pygame.quit()
