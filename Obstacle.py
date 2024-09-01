import pygame
import Textures_src
from config import *


class Obstacle():
    def __init__(self, position):
        self._position = position
        self.rect = pygame.rect.Rect(
            position[0],
            position[1],
            TILE_LEN, TILE_LEN
        )
        self.icon = pygame.image.load(Textures_src.OBSTACLE)
        if TILE_LEN > 20:
            scale = TILE_LEN // 20
            self.icon = pygame.transform.scale_by(self.icon, scale)

    def draw(self, screen):
        screen.blit(self.icon, (self.rect.x, self.rect.y))

    def set_position(self, position):
        self.rect.x = position[0]
        self.rect.y = position[1]
        self._position = position

    def get_position(self):
        return self._position
