import pygame

class PausedGameScreen(pygame.Surface):
    def __init__(self, x, y):
        super().__init__((x,y))
        self.font = pygame.font.SysFont("Arial", 30)
        self.text = self.font.render("Paused", False, "Black")
        
        self.color = "#444444"
        self.fill(self.color)
        
    def display(self, screen):
        self.blit(self.text, ((self.get_width()//2)-(self.text.get_width()//2),self.get_height()//2))