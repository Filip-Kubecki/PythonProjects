import pygame
import Textures_src
from config import *


class Apple():
    def __init__(self):
        self.rect = pygame.rect.Rect(10000, 10000, TILE_LEN, TILE_LEN)
        self.appleIcon = pygame.image.load(Textures_src.APPLE)
        if TILE_LEN > 20:
            scale = TILE_LEN // 20
            self.appleIcon = pygame.transform.scale_by(self.appleIcon, scale)
        self.position = (10000, 10000)

    def draw_apple(self, screen):
        screen.blit(self.appleIcon, (self.rect.x, self.rect.y))

    def set_position(self, position):
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.position = position
