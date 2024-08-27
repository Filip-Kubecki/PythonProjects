import pygame
import tools
import Textures_src
import config
from Snake import Snake
from Apple import Apple


class GameInstance(pygame.Surface):
    def __init__(self):
        self.elements = list()

        # List containing free spaces
        self.free_fields = list()
        for i in range((config.GAME_INSTANCE_WIDTH//20)*(config.GAME_INSTANCE_HEIGHT//20)):
            self.free_fields.append(i)

        self.score = 0
        self.screen = pygame.surface.Surface(
            (config.GAME_INSTANCE_WIDTH,
             config.GAME_INSTANCE_HEIGHT)
        )

        # Backgroung setup
        self._bgTile = pygame.image.load(Textures_src.BACKGROUND_GAME_TILE)
        tools.tileBackground(self.screen, self._bgTile)

        # Snake object setup
        self.snake = Snake(
            self.screen.get_width() // 2,
            self.screen.get_height() // 2
        )
        self.elements.append(self.snake)

        # Apple object setup
        self.apple = Apple()
        self.apple.set_random_position(self.screen)
        self.elements.append(self.apple)

    def run_game_cycle(self):
        # fill the screen with a color to wipe away anything from last frame
        tools.tileBackground(self.screen, self._bgTile)

        # Draw apple object
        self.apple.draw_apple(self.screen)

        # Draw snake object
        self.snake.draw_snake(self.screen)

        keys = pygame.key.get_pressed()

        self.snake.key_event(keys)

    def snake_collision_game_over(self):
        if self.snake.self_collision(self.screen):
            return True
        return False

    def snake_update(self):
        self.snake.update(self.screen)

    def apple_eaten(self):
        # Checking if Snake eats Apple
        if self.apple.rect.colliderect(self.snake.segments[0].rect):
            self.snake.add_segment()
            self.apple.set_random_position(self.screen)
            return True
        return False
