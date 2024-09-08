import pygame
import resources
from config import *
from resources import TexturesSrc


class Apple():
    def __init__(self):
        self.rect = pygame.rect.Rect(10000, 10000, TILE_LEN, TILE_LEN)
        self._appleIcon = pygame.image.load(TexturesSrc.APPLE)
        if TILE_LEN > 20:
            scale = TILE_LEN // 20
            self._appleIcon = pygame.transform.scale_by(self._appleIcon, scale)
        self.position = (10000, 10000)

    def draw_apple(self, screen):
        screen.blit(self._appleIcon, (self.rect.x, self.rect.y))

    def set_position(self, position):
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.position = position
