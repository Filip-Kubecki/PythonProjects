import pygame
import Style
import tools
import pygame.freetype
import Textures_src
from GameInstance import GameInstance
from PausedGameScreen import PausedGameScreen
from GameOverScreen import GameOverScreen
from Button import Button

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
pause_oppacity = 0

# Game Over screen
game_over_screen = GameOverScreen(SCREEN_WIDTH, SCREEN_HEIGHT)

# Game variables
delta_time = 0  # time in seconds since last frame - used for limiting FPS
counter = 0

game_started = False
pause_game = False
game_over = False
game_tick = 10

score = 0

# UI elements
apple_icon = pygame.image.load(Textures_src.APPLE)
apple_icon = pygame.transform.scale_by(apple_icon, 1.6)

ui_font = pygame.freetype.SysFont('JetBrainsMono NFM, thin', 28)
random_button = Button(40, 40, Textures_src.BACKGROUND_GAME_TILE)

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

    # Self collision - game over
    if board.snake_collision_game_over():
        game_over = True

    # Main surface background
    screen.fill(Style.DARK_GREEN)
    pygame.draw.rect(  # Border around board
        screen,
        Style.DARK_BROWN,   # Color of the border
        pygame.Rect(20, 70, 810, 610),
        7,              # Border width
        7               # Border radius
    )

    # Display UI elements
    screen.blit(apple_icon, (35, 20))
    ui_font.render_to(
        screen,
        (75, 28),
        score.__str__(),
        Style.CREAMY_WHITE
    )
    random_button.display(screen)
    random_button.mouse_click(tools.shit)

    # Run one board cycle
    board.run_game_cycle()

    # Check if snake ate apple - increase score
    if board.apple_eaten():
        score += 10

    # Taking keyboard input
    keys = pygame.key.get_pressed()

    game_tick = tools.game_pace(keys, game_tick)

    # Start game when WSAD pressed
    if (keys[pygame.K_w] or
        keys[pygame.K_s] or
        keys[pygame.K_a] or
            keys[pygame.K_d]):
        game_started = True

    # Update state of snake: position and directions of segments
    if counter >= game_tick:
        counter = 0
        if not pause_game and not game_over and game_started:
            board.snake_update()

    # Display game instance surface
    screen.blit(board.screen, (25, 75))

    # Display GameOver screen
    if game_over:
        screen.blit(
            game_over_screen,
            tools.two_surfaces_centering_offset(screen, game_over_screen))
        game_over_screen.display(screen)

    # display pause screen
    if pause_game and not game_over:
        if pause_oppacity < 150:
            pause_oppacity += 15

        pause_screen.fill((20, 20, 20, pause_oppacity))
        screen.blit(
            pause_screen,
            tools.two_surfaces_centering_offset(screen, pause_screen)
        )
        pause_screen.display(screen)
    else:
        pause_oppacity = 0

    # Update everything on screen
    pygame.display.flip()

    # Update in game timmer
    counter += 1

    # limits FPS to 60
    delta_time = clock.tick(60) / 1000

pygame.quit()
