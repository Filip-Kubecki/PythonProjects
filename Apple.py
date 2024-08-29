import pygame
import Textures_src


class Apple():
    def __init__(self):
        self.rect = pygame.rect.Rect(10000, 10000, 20, 20)
        self.appleIcon = pygame.image.load(Textures_src.APPLE)
        self.position = (10000, 10000)

    def draw_apple(self, screen):
        screen.blit(self.appleIcon, (self.rect.x, self.rect.y))

    def set_position(self, position):
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.position = position
