import pygame
from tools import Direction

class Apple():
    def __init__(self):
        self.color = "#ff0000"
        self.rect = pygame.pygame.rect.Rect(-100, -100, 20, 20)