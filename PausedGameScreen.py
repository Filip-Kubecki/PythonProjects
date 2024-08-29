import pygame
import pygame.freetype
import Textures_src
import Style
import config
from Button import Button


class PausedGameScreen(pygame.Surface):
    def __init__(self, x, y):
        super().__init__((x, y), pygame.SRCALPHA)
        self.title_font = pygame.freetype.SysFont('JetBrainsMono NT', 60)
        self.font = pygame.freetype.SysFont('JetBrainsMono NFP', 32)

        # Setting up transparent background
        self.convert_alpha()
        self.fill((20, 20, 20))
        self.set_alpha(0)

        # Title
        self.title = "Pause"

        # Menu buttno background
        self.menu_background = pygame.Rect(225, 300, 400, 100)

        # Menu buttons
        self.exit_icon = Button(65, 65, (525, 325), Textures_src.UI_EXIT_ICON)
        self.option_icon = Button(
            55, 55, (400, 325), Textures_src.UI_OPTION_ICON)
        self.restart_icon = Button(
            55, 55, (275, 325), Textures_src.UI_RESTART_ICON)

        self.buttons = list()
        self.buttons.append(self.restart_icon)
        self.buttons.append(self.option_icon)
        self.buttons.append(self.exit_icon)

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

        self.exit_icon.display(screen)
        self.option_icon.display(screen)
        self.restart_icon.display(screen)

        self.exit_icon.hover()
        self.option_icon.hover()
        self.restart_icon.hover()

        for button in self.buttons:
            button.set_alpha(255)

        if self.in_focus is not None:
            self.buttons[self.in_focus].set_alpha(
                config.DIMMED_BACKGROUND_MAX_ALPHA)

    def next_focused(self):
        if self.in_focus is None:
            self.in_focus = 0
        elif self.in_focus < len(self.buttons)-1:
            self.in_focus += 1
        else:
            self.in_focus = 0

    def none_focused(self):
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
