import pygame
import pygame.freetype
import resources
from resources import TexturesSrc
from resources import Style
from config import *
from Button import Button


class PausedGameScreen(pygame.Surface):
    def __init__(self, x, y):
        super().__init__((x, y), pygame.SRCALPHA)

        self._title_font = pygame.freetype.Font(
            "resources/font/JetBrainsMonoNL-Regular.ttf", 80)

        # Setting up transparent background
        self.convert_alpha()
        self.fill((20, 20, 20))
        self.set_alpha(0)

        # Title
        self._title = "Pause"

        # Menu buttons
        button_size = PAUSE_SCREEN_BUTTON_SIZE
        center_element_width = (WINDOW_WIDTH/2)-(button_size/2)
        screen_center_y = WINDOW_HEIGHT/2
        button_y = screen_center_y-(button_size/2)

        self.restart_icon = Button(
            button_size, button_size,
            (center_element_width-button_size-PAUSE_SCREEN_BUTTON_OFFSET, button_y),
            TexturesSrc.UI_RESTART_ICON
        )
        self.option_icon = Button(
            button_size, button_size,
            (center_element_width, button_y),
            TexturesSrc.UI_OPTION_ICON
        )
        self.exit_icon = Button(
            button_size, button_size,
            ((center_element_width+button_size+PAUSE_SCREEN_BUTTON_OFFSET), button_y),
            TexturesSrc.UI_EXIT_ICON
        )

        # Menu buttno background
        self.menu_background = pygame.Rect(
            (WINDOW_WIDTH/2)-(PAUSE_SCREEN_BUTTON_MENU_WIDTH/2),
            screen_center_y-(PAUSE_SCREEN_BUTTON_MENU_HEIGHT/2),
            PAUSE_SCREEN_BUTTON_MENU_WIDTH,
            PAUSE_SCREEN_BUTTON_MENU_HEIGHT
        )

        self.buttons = list()
        self.buttons.append(self.restart_icon)
        self.buttons.append(self.option_icon)
        self.buttons.append(self.exit_icon)

        self.in_focus = None

    def display(self, screen):
        self._title_font.render_to(
            screen,
            ((screen.get_width() // 2) -
             (self._title_font.get_rect(self._title).width // 2), self.menu_background.y-120),
            self._title,
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
            self.buttons[self.in_focus].set_alpha(DIMMED_BACKGROUND_MAX_ALPHA)

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
            if self.get_alpha() < DIMMED_BACKGROUND_MAX_ALPHA:
                self.set_alpha(
                    self.get_alpha() + DIMMED_BACKGROUND_ALPHA_INCREMENT
                )

    def hide_background(self):
        self.set_alpha(0)
