import pygame
import tools
import Textures_src
from config import *
from Snake import Snake
from Apple import Apple
from random import randrange


class GameInstance(pygame.Surface):
    def __init__(self):
        print("Game instance initialization ---------------")
        self.obstacles = list()

        self.screen = pygame.surface.Surface(
            (GAME_INSTANCE_WIDTH, GAME_INSTANCE_HEIGHT)
        )

        # Initializing list with all possible positions on board
        self._position_indexes = list()
        for i in range((GAME_INSTANCE_WIDTH//TILE_LEN)*(GAME_INSTANCE_HEIGHT//TILE_LEN)):
            self._position_indexes.append(i)

        # Backgroung setup
        self._bgTile = pygame.image.load(Textures_src.BACKGROUND_GAME_TILE)
        if TILE_LEN > 20:
            scale = TILE_LEN // 20
            self._bgTile = pygame.transform.scale_by(self._bgTile, scale)

        tools.tileBackground(self.screen, self._bgTile)

        # Snake object setup
        self.snake = Snake(
            (GAME_INSTANCE_WIDTH // 2) -
            ((GAME_INSTANCE_WIDTH // 2) % TILE_LEN),
            (GAME_INSTANCE_HEIGHT // 2) -
            ((GAME_INSTANCE_HEIGHT // 2) % TILE_LEN)
        )

        # Apple object setup
        self.apple = Apple()
        self.place_apple()

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
            self.snake.add_segment(self)
            self.place_apple()
            return True
        return False

    def place_apple(self):
        free_indexes = self._position_indexes.copy()

        snake_indexes = self.snake.get_position_indexes()

        for i in (range(len(snake_indexes)-1)):
            free_indexes.remove(snake_indexes[i])

        random_index = tools.index_to_position(
            free_indexes[randrange(0, len(free_indexes))]
        )
        self.apple.set_position(random_index)
