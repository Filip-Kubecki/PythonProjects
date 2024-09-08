import pygame.freetype
import tools
import pygame
from GameOverScreen import GameOverScreen
from PausedGameScreen import PausedGameScreen
from GameInstance import GameInstance
from config import *
from resources import TexturesSrc, Style


class GameWrapper(pygame.Surface):
    def __init__(self, width, height):
        super().__init__((width, height), pygame.SRCALPHA)

        self._board = GameInstance()
        self.pause_screen = PausedGameScreen(width, height)
        self.game_over_screen = GameOverScreen(width, height)

        self._in_game_clock = 0
        self._counter = 0
        self._pause_game = False
        self._game_over = False
        self._game_started = False
        self._game_tick = SNAKE_START_SPEED
        self._score = 0
        self.running = True

        # UI elements
        self._apple_icon = pygame.image.load(TexturesSrc.APPLE)
        self._apple_icon = pygame.transform.scale_by(
            self._apple_icon,
            GAME_INSTANCE_SCALE
        )

        # Border
        self._border = pygame.image.load(TexturesSrc.BORDER)

        self._score_font = pygame.freetype.Font(
            "resources/font/JetBrainsMonoNL-Medium.ttf", 16*GAME_INSTANCE_SCALE)

# -----------------------------------------------------------------------------------
    def set_pause_game(self, value):
        self._pause_game = value

    def get_pause_game(self):
        return self._pause_game

    def set_game_over(self, value):
        self._game_over = value

    def get_game_over(self):
        return self._game_over

    def game_cycle(self):
        # Displays ui elements
        self.display_ui()

        # Self collision check - game over
        if self._board.snake_collision_game_over():
            self._game_over = True

        # Obstacle collision - game over
        if self._board.obstacle_draw_and_check_collision():
            self._game_over = True

        # Run one board cycle
        self._board.run_game_cycle()

        # Check if snake apple eaten - increase score
        if self._board.apple_eaten():
            self._score += 1

        # Taking keyboard input
        keys = pygame.key.get_pressed()
        self.change_game_speed(keys)
        self.start_game(keys)

        # Update state of snake: position and directions of segments
        if self._counter >= self._game_tick:
            self._counter = 0
            if not self._pause_game and not self._game_over and self._game_started:
                self._board.snake_update()

        # Display game instance surface
        self.blit(
            self._board.screen,
            (   # Position
                tools.two_surfaces_centering_offset(
                    self, self._board.screen)[0],
                GAME_INSTANCE_TOP_MARGIN
            )
        )

        self.enable_border()

        self.check_for_game_over(keys)
        self.check_for_pause(keys)

        self._counter += 1

    def display_ui(self):
        # Main surface background
        self.fill(Style.DARK_GREEN)
        pygame.draw.rect(  # Border around board
            self,
            # Color of the border
            Style.DARK_BROWN if not GAME_INSTANCE_BORDER_COLLISION else Style.DARK_RED,
            pygame.Rect(
                (WINDOW_WIDTH-(GAME_INSTANCE_WIDTH +
                               (GAME_INSTANCE_BORDER_WIDTH*2)))//2,   # X position
                GAME_INSTANCE_TOP_MARGIN-GAME_INSTANCE_BORDER_WIDTH,      # Y position
                GAME_INSTANCE_WIDTH + (GAME_INSTANCE_BORDER_WIDTH*2),   # Width
                GAME_INSTANCE_HEIGHT +
                (GAME_INSTANCE_BORDER_WIDTH*2)   # Height
            ),
            GAME_INSTANCE_BORDER_WIDTH,              # Border width
            7               # Border radius
        )
        # Display UI elements
        self.blit(self._apple_icon, (55, 20))
        self._score_font.render_to(
            self,
            (125, 32),
            self._score.__str__(),
            Style.CREAMY_WHITE
        )

    def enable_border(self):
        if ENABLE_BORDER:
            border_size = self._border.get_size()
            self.blit(
                self._border,
                (GAME_INSTANCE_WIDTH - border_size[0],
                 GAME_INSTANCE_TOP_MARGIN-border_size[1]+20)
            )

    def check_for_game_over(self, keys):
        if self._game_over:
            self.game_over_screen.dim_background()
            self.blit(
                self.game_over_screen,
                tools.two_surfaces_centering_offset(self, self.game_over_screen))
            self.game_over_screen.display(self)

            if self.game_over_screen.restart_icon.mouse_click():
                self._board = GameInstance()
                self._score = 0
                self._game_started = False
                self._game_over = False

            if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
                if self.game_over_screen.in_focus is not None:
                    self._board = GameInstance()
                    self._score = 0
                    self._game_started = False
                    self._game_over = False
        else:
            self.game_over_screen.hide_background()
            self.game_over_screen.unfocus()

    def check_for_pause(self, keys):
        if self._pause_game and not self._game_over:
            self.pause_screen.dim_background()
            self.blit(
                self.pause_screen,
                tools.two_surfaces_centering_offset(self, self.pause_screen)
            )
            self.pause_screen.display(self)

            if self.pause_screen.exit_icon.mouse_click():
                self.running = False
            elif self.pause_screen.restart_icon.mouse_click():
                self._board = GameInstance()
                self._score = 0
                self._game_started = False
                self._pause_game = False

            if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
                match self.pause_screen.in_focus:
                    case 2:
                        self.running = False
                    case 1:
                        # TODO: add options menu
                        print("TODO: THIS THING")
                    case 0:
                        self._board = GameInstance()
                        self._score = 0
                        self._game_started = False
                        self._pause_game = False
        else:
            self.pause_screen.hide_background()
            self.pause_screen.none_focused()

    def change_game_speed(self, keys):
        if keys[pygame.K_1]:
            self._game_tick = 60
        elif keys[pygame.K_2]:
            self._game_tick = SNAKE_START_SPEED
        elif keys[pygame.K_3]:
            self._game_tick = 3
        elif keys[pygame.K_EQUALS]:
            self._game_tick += 1
        elif keys[pygame.K_MINUS] and self._game_tick > 0:
            self._game_tick

    def start_game(self, keys):
        if (keys[pygame.K_w] or
            keys[pygame.K_d] or
            keys[pygame.K_a] or
            keys[pygame.K_LEFT] or
            keys[pygame.K_RIGHT] or
                keys[pygame.K_UP]):
            self._game_started = True
