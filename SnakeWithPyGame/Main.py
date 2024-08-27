import pygame
import Style
import tools
import pygame.freetype
import Textures_src
import config
from GameInstance import GameInstance
from PausedGameScreen import PausedGameScreen
from GameOverScreen import GameOverScreen


# Pygame setup
pygame.init()
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
running = True

# Create Board object
board = GameInstance()

# Pause screen
pause_screen = PausedGameScreen(config.WINDOW_WIDTH, config.WINDOW_HEIGHT)

# Game Over screen
game_over_screen = GameOverScreen(config.WINDOW_WIDTH, config.WINDOW_HEIGHT)

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

# Main loop of game -----------------------------------------------------------
while running:
    # pygame.QUIT event means the user clicked X to close window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                counter = 0
                pause_game = not pause_game

            if pause_game and event.key == pygame.K_TAB:
                pause_screen.next_focused()

            if game_over and event.key == pygame.K_TAB:
                game_over_screen.focus()

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
        game_over_screen.dim_background()
        screen.blit(
            game_over_screen,
            tools.two_surfaces_centering_offset(screen, game_over_screen))
        game_over_screen.display(screen)

        if game_over_screen.restart_icon.mouse_click():
            board = GameInstance()
            score = 0
            game_started = False
            game_over = False

        if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
            if game_over_screen.in_focus is not None:
                board = GameInstance()
                score = 0
                game_started = False
                game_over = False
    else:
        game_over_screen.hide_background()
        game_over_screen.unfocus()

    # display pause screen
    if pause_game and not game_over:
        pause_screen.dim_background()
        screen.blit(
            pause_screen,
            tools.two_surfaces_centering_offset(screen, pause_screen)
        )
        pause_screen.display(screen)

        if pause_screen.exit_icon.mouse_click():
            running = False
        elif pause_screen.restart_icon.mouse_click():
            board = GameInstance()
            score = 0
            game_started = False
            pause_game = False

        if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
            match pause_screen.in_focus:
                case 2:
                    running = False
                case 1:
                    print("TODO: THIS THING")
                case 0:
                    board = GameInstance()
                    score = 0
                    game_started = False
                    pause_game = False
    else:
        pause_screen.hide_background()
        pause_screen.none_focused()

    # Update everything on screen
    pygame.display.flip()

    # Update in game timmer
    counter += 1

    # limits FPS to 120
    delta_time = clock.tick(120) / 1000

pygame.quit()
