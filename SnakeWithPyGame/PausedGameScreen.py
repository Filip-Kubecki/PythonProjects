import pygame
import pygame.freetype

import tools


class PausedGameScreen(pygame.Surface):
    def __init__(self, x, y):
        super().__init__((x, y), pygame.SRCALPHA)
        self.title_font = pygame.freetype.SysFont('JetBrainsMono NT', 50)
        self.font = pygame.freetype.SysFont('JetBrainsMono NFP', 32)

        self.title = "Paused"
        self.text_rect = self.title_font.get_rect(self.title)

        self.exit = "Exit"

        self.convert_alpha()
        self.fill((20, 20, 20, 150))

    def display(self, screen):
        self.title_font.render_to(
            screen,
            ((screen.get_width() // 2) -
             (self.title_font.get_rect(self.title).width // 2), 250),
            self.title,
            "black"
        )

        self.font.render_to(
            screen,
            (tools.two_values_centering_offset(screen.get_width(), self.font.get_rect(self.exit).width),
             400),
            self.exit,
            "black"
        )
