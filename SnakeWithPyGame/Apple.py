import pygame
import random
from tools import Direction

class Apple():
    def __init__(self):
        self.color = "#03d3ff"
        self.rect = pygame.rect.Rect(10000, 10000, 20, 20)

    def draw_apple(self, screen):
        pygame.draw.rect(screen, self.color, self.rect) 

    def set_random_position(self, screen):
        self.rect.x = random.randrange(0, screen.get_width(), 20)
        self.rect.y = random.randrange(0, screen.get_height(), 20)