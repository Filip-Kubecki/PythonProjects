import pygame
import pygame.freetype
import Textures_src
import Style


class PausedGameScreen(pygame.Surface):
    def __init__(self, x, y):
        super().__init__((x, y), pygame.SRCALPHA)
        self.title_font = pygame.freetype.SysFont('JetBrainsMono NT', 60)
        self.font = pygame.freetype.SysFont('JetBrainsMono NFP', 32)

        # Title
        self.title = "Paused"
        self.text_rect = self.title_font.get_rect(self.title)

        # Menu buttno background
        self.menu_background = pygame.Rect(225, 300, 400, 100)

        # Menu buttons
        self.exit_icon = pygame.image.load(Textures_src.UI_EXIT_ICON)
        self.exit_icon = pygame.transform.scale_by(self.exit_icon, 0.1)
        self.option_icon = pygame.image.load(Textures_src.UI_OPTION_ICON)
        self.option_icon = pygame.transform.scale_by(self.option_icon, 0.1)
        self.restart_icon = pygame.image.load(Textures_src.UI_RESTART_ICON)
        self.restart_icon = pygame.transform.scale_by(self.restart_icon, 0.1)

        self.convert_alpha()

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

        screen.blit(self.restart_icon, (275, 325))
        screen.blit(self.option_icon, (400, 325))
        screen.blit(self.exit_icon, (525, 325))
