import pygame
import random
from tools import Direction


class Apple():
    def __init__(self):
        self.rect = pygame.rect.Rect(10000, 10000, 20, 20)
        self.appleIcon = pygame.image.load(
            '/home/bork/PythonProjects/SnakeWithPyGame/img/apple.png')

    def draw_apple(self, screen):
        screen.blit(self.appleIcon, (self.rect.x, self.rect.y))

    def set_random_position(self, screen):
        self.rect.x = random.randrange(0, screen.get_width(), 20)
        self.rect.y = random.randrange(0, screen.get_height(), 20)
