import pygame
import pygame.freetype

class PausedGameScreen(pygame.Surface):
    def __init__(self, x, y):
        super().__init__((x,y), pygame.SRCALPHA)
        self.font = pygame.freetype.SysFont('Sans', 50)

        self.text = "Paused"
        self.text_rect = self.font.get_rect(self.text)
        # self.convert_alpha()
        self.fill((168, 168, 168, 150))
        
    def display(self, screen):
        self.font.render_to(screen, ((screen.get_width() // 2)-(self.text_rect.width // 2), 150), self.text, "black")
        # self.blit(self.text, ((self.get_width() // 2)-(self.text.get_width() // 2), 50))