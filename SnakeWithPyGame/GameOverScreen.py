import pygame
from pygame.display import Info
import pygame.freetype
import Textures_src
import Style
import config
from Button import Button


class GameOverScreen(pygame.Surface):
    def __init__(self, x, y):
        super().__init__((x, y), pygame.SRCALPHA)
        self.title_font = pygame.freetype.SysFont('JetBrainsMono NT', 60)

        # Setting up transparent background
        self.convert_alpha()
        self.fill((20, 20, 20))
        self.set_alpha(0)

        # Title
        self.title = "Game over"

        # Menu buttno background
        self.menu_background = pygame.Rect(350, 300, 150, 100)

        self.restart_icon = Button(
            55, 55, (400, 325), Textures_src.UI_RESTART_ICON)

        self.in_focus = None

    def display(self, screen):
        self.title_font.render_to(
            screen,
            ((screen.get_width() // 2) -
             (self.title_font.get_rect(self.title).width // 2), 225),
            self.title,
            Style.MOSSE_GREEN
        )

        pygame.draw.rect(
            screen,
            Style.LIGHT_GREEN,
            self.menu_background,
            border_radius=25
        )

        self.restart_icon.display(screen)

        self.restart_icon.hover()

        if self.in_focus is not None:
            self.restart_icon.set_alpha(config.DIMMED_BACKGROUND_MAX_ALPHA)
        else:
            self.restart_icon.set_alpha(255)

    def focus(self):
        self.in_focus = self.restart_icon

    def unfocus(self):
        self.in_focus = None

    def dim_background(self):
        if self.get_alpha() is None:
            raise Exception("No alpha value exeption")
        else:
            if self.get_alpha() < config.DIMMED_BACKGROUND_MAX_ALPHA:
                self.set_alpha(
                    self.get_alpha() + config.DIMMED_BACKGROUND_ALPHA_INCREMENT
                )

    def hide_background(self):
        self.set_alpha(0)
