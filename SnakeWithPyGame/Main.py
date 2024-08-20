import pygame
from Snake import Snake
from PausedGameScreen import PausedGameScreen
from GameOverScreen import GameOverScreen
from Apple import Apple
import tools

# Pygame setup
pygame.init()
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 800))
running = True

# Backgroung setup
bgTile = pygame.image.load(
    '/home/bork/PythonProjects/SnakeWithPyGame/img/backgroundTile.png')
tools.tileBackground(screen, bgTile)

# Snake object setup
snake = Snake(screen.get_width() // 2, (screen.get_height() // 2))

# Apple object setup
apple = Apple()
apple.set_random_position(screen)

# Pause screen
pause_screen = PausedGameScreen(300, 400)

# Pause screen
game_over_screen = GameOverScreen(300, 300)

# Game variables
dt = 0
counter = 0
pause_game = False
game_over = False
gameTick = 15


# Main loop of game -------------------------------------------------------------------------
while running:
    # pygame.QUIT event means the user clicked X to close window
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                counter = 0
                pause_game = not pause_game
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    tools.tileBackground(screen, bgTile)

    # Draw apple object
    apple.draw_apple(screen)

    # Draw snake object
    snake.draw_snake(screen)

    # display pause screen
    if pause_game:
        screen.blit(pause_screen, ((screen.get_width()//2)-(pause_screen.get_width()//2),
                    (screen.get_height()//2)-(pause_screen.get_height()//2)))
        pause_screen.display(screen)

    # Snake reacting to key events
    keys = pygame.key.get_pressed()
    snake.key_event(keys)

    # Change pace of the game
    if keys[pygame.K_p]:
        gameTick = 60
    elif keys[pygame.K_o]:
        gameTick = 15
    elif keys[pygame.K_i]:
        gameTick = 8

    # Update state of snake: position and directions of segments
    if counter >= gameTick:
        counter = 0
        if not pause_game and not game_over:
            snake.update(screen)

    # Snake eats apple
    if apple.rect.colliderect(snake.segments[0].rect):
        snake.add_segment()
        apple.set_random_position(screen)

    # Self collision - game over
    if snake.self_collision():
        screen.blit(game_over_screen, ((screen.get_width()//2)-(game_over_screen.get_width()//2),
                    (screen.get_height()//2)-(game_over_screen.get_height()//2)))
        game_over_screen.display(screen)
        game_over = True

    # Update everything on screen
    pygame.display.flip()

    # Update in game timmer
    counter += 1

    # limits FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()
