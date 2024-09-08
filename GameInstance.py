import pygame
import tools
from config import *
from Snake import Snake
from Apple import Apple
from random import randrange
from resources import TexturesSrc, Style


class GameInstance(pygame.Surface):
    def __init__(self):
        print("Game instance initialization ---------------")

        self.screen = pygame.surface.Surface(
            (GAME_INSTANCE_WIDTH, GAME_INSTANCE_HEIGHT)
        )

        # Initializing list with all possible positions on board
        self._position_indexes = list()
        for i in range((GAME_INSTANCE_WIDTH//TILE_LEN)*(GAME_INSTANCE_HEIGHT//TILE_LEN)):
            self._position_indexes.append(i)

        # Obstacle setup
        self.obstacles = list()
        # self.obstacles = tools.generate_obstacle_border()

        # Backgroung setup
        self._bgTile = pygame.image.load(TexturesSrc.BACKGROUND_GAME_TILE)
        if TILE_LEN > 20:
            scale = TILE_LEN // 20
            self._bgTile = pygame.transform.scale_by(self._bgTile, scale)

        tools.tileBackground(self.screen, self._bgTile)

        # Snake object setup
        self._snake = Snake(
            (GAME_INSTANCE_WIDTH // 2) -
            ((GAME_INSTANCE_WIDTH // 2) % TILE_LEN),
            (GAME_INSTANCE_HEIGHT // 2) -
            ((GAME_INSTANCE_HEIGHT // 2) % TILE_LEN)
        )

        # Apple object setup
        self._apple = Apple()
        self.place_apple()

    def run_game_cycle(self):
        # fill the screen with a color to wipe away anything from last frame
        tools.tileBackground(self.screen, self._bgTile)

        # Draw obstacles
        self.obstacle_draw_and_check_collision()

        # Draw apple object
        self._apple.draw_apple(self.screen)

        # Draw snake object
        self._snake.draw_snake(self.screen)

        keys = pygame.key.get_pressed()

        self._snake.key_event(keys)

    def snake_collision_game_over(self):
        if self._snake.self_collision(self.screen):
            return True
        return False

    def snake_update(self):
        self._snake.update(self.screen)

    def apple_eaten(self):
        # Checking if Snake eats Apple
        if self._apple.rect.colliderect(self._snake.segments[0].rect):
            self._snake.add_segment(self)
            self.place_apple()
            return True
        return False

    def place_apple(self):
        free_indexes = self._position_indexes.copy()
        if len(free_indexes) <= 2:
            print("WIN")
            return
        limit = free_indexes[-1]

        snake_indexes = self._snake.get_position_indexes().copy()

        for i in snake_indexes:
            if i <= limit:
                free_indexes.remove(i)

        for i in self.obstacles:
            free_indexes.remove(tools.position_to_index(i.get_position()))

        if free_indexes:
            random_index = tools.index_to_position(
                free_indexes[randrange(0, len(free_indexes))]
            )
            self._apple.set_position(random_index)

    def obstacle_draw_and_check_collision(self):
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)
            if obstacle.rect.colliderect(self.snake.segments[0].rect):
                self.snake.decapitate(self.screen)
                return True
        return False
