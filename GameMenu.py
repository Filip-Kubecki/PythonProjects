import pygame
import pygame.freetype
from Button import Button
from resources import TexturesSrc, Style


class GameMenu(pygame.Surface):
    def __init__(self, width, height):
        super().__init__((width, height))

        self.fill(Style.DARK_GREEN)

        # Title banner
        self._snake_banner = pygame.image.load(TexturesSrc.MAIN_MENU_BANNER)
        self.blit(
            self._snake_banner,
            ((width//2)-(self._snake_banner.get_width()//2), 125)
        )

        # Setting up buttons
        self._button_font = pygame.freetype.Font(
            "resources/font/JetBrainsMonoNL-Regular.ttf", 56)
        button_x_center = (width // 2) - 200

        self._play_button = Button(
            400, 100,   # Button size
            (button_x_center, 350),   # Button position
            text="Play",
            font=self._button_font
        )
        self._play_button.set_alpha(255)
        self._option_button = Button(
            400, 100,   # Button size
            (button_x_center, 500),   # Button position
            text="Options",
            font=self._button_font
        )
        self._quit_button = Button(
            400, 100,   # Button size
            (button_x_center, 650),   # Button position
            text="Quit",
            font=self._button_font
        )
        self._buttons = list()
        self._buttons.append(self._play_button)
        self._buttons.append(self._option_button)
        self._buttons.append(self._quit_button)

    def display(self, screen):
        self._play_button.hover()
        self._option_button.hover()
        self._quit_button.hover()

        self._play_button.display(self)
        self._option_button.display(self)
        self._quit_button.display(self)

        screen.blit(self, (0, 0))
