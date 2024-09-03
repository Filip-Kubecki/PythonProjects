import pygame
import pygame.freetype
import Style


class Game_menu(pygame.Surface):
    def __init__(self, x, y):
        super().__init__((x, y))

        self.title_font = pygame.freetype.SysFont('JetBrainsMono NT', 60)
        self._title_text = "Snake"

    def display(self):
        self.title_font.render_to(
            self,
            ((self.get_width() // 2) -
             (self.title_font.get_rect(self._title_text).width // 2), 100),
            self._title_text,
            Style.MOSSE_GREEN
        )
