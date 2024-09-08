import pygame
from config import *
from resources import Style, TexturesSrc


class Obstacle():
    def __init__(self, position):
        self._position = position
        self.rect = pygame.rect.Rect(
            position[0],
            position[1],
            TILE_LEN, TILE_LEN
        )
        self._icon = pygame.image.load(TexturesSrc.OBSTACLE)
        if TILE_LEN > 20:
            scale = TILE_LEN // 20
            self._icon = pygame.transform.scale_by(self._icon, scale)

    def draw(self, screen):
        screen.blit(self.icon, (self.rect.x, self.rect.y))

    def set_position(self, position):
        self.rect.x = position[0]
        self.rect.y = position[1]
        self._position = position

    def get_position(self):
        return self._position
