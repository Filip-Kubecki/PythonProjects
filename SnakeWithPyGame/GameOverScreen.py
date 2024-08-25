import pygame
import pygame.freetype


class GameOverScreen(pygame.Surface):
    def __init__(self, x, y):
        super().__init__((x, y), pygame.SRCALPHA)
        self.font = pygame.freetype.SysFont('Sans', 50)

        self.text = "Game Over"
        self.text_rect = self.font.get_rect(self.text)
        # self.convert_alpha()
        self.fill((20, 20, 20, 150))

    def display(self, screen):
        self.font.render_to(
            screen,
            ((screen.get_width() // 2)-(self.text_rect.width // 2),
             (screen.get_height() // 2)-50),
            self.text,
            "black")
