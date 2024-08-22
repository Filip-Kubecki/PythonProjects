from enum import Enum
import pygame
import math


def tileBackground(screen: pygame.display, image: pygame.Surface):
    screenWidth, screenHeight = screen.get_size()
    imageWidth, imageHeight = image.get_size()

    # Calculate how many tiles we need to draw in x axis and y axis
    tilesX = math.ceil(screenWidth / imageWidth)
    tilesY = math.ceil(screenHeight / imageHeight)

    # Loop over both and blit accordingly
    for x in range(tilesX):
        for y in range(tilesY):
            screen.blit(image, (x * imageWidth, y * imageHeight))


class Direction(Enum):
    NONE = 0
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4


class Snake_texture_state(Enum):
    HEAD = 1
    SEGMENT = 2
    TAIL = 3
    UP_LEFT = 4
    UP_RIGHT = 5
    DOWN_LEFT = 6
    DOWN_RIGHT = 7
