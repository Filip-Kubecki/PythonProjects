from enum import Enum
import pygame
import math
from Obstacle import Obstacle
from config import *


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


def two_surfaces_centering_offset(outer_surface, inner_surface):
    x_offset = (outer_surface.get_width()//2)-(inner_surface.get_width()//2)
    y_offset = (outer_surface.get_height()//2)-(inner_surface.get_height()//2)
    return (x_offset, y_offset)


def two_values_centering_offset(outer_value, inner_value):
    return ((outer_value // 2) - (inner_value // 2))


def game_pace(keys, game_tick):
    # Change pace of the game
    if keys[pygame.K_1]:
        game_tick = 60
    elif keys[pygame.K_2]:
        game_tick = SNAKE_START_SPEED
    elif keys[pygame.K_3]:
        game_tick = 5
    elif keys[pygame.K_EQUALS]:
        game_tick += 1
    elif keys[pygame.K_MINUS] and game_tick > 0:
        game_tick -= 1

    return game_tick


def check_if_mouse_collide(mouse_pos, object_pos, object_size):
    # print(mouse_pos, object_pos, object_size)
    if (mouse_pos[0] > object_pos[0] and
        mouse_pos[0] <= object_pos[0]+object_size[0] and
            mouse_pos[1] > object_pos[1] and
            mouse_pos[1] <= object_pos[1]+object_size[1]):
        return True

    return False


def mouse_button_down():
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            return True

    return False


def index_to_position(index):
    return (
        (index % (GAME_INSTANCE_WIDTH//TILE_LEN)) *
        TILE_LEN,  # x position
        (index // (GAME_INSTANCE_WIDTH//TILE_LEN)) *
        TILE_LEN  # y position
    )


def position_to_index(position):
    return ((position[0]//TILE_LEN) +
            ((position[1]//TILE_LEN)*(GAME_INSTANCE_WIDTH//TILE_LEN)))


def generate_obstacle_border():
    obstacles = list()
    for i in range(GAME_INSTANCE_WIDTH//TILE_LEN):
        obstacles.append(Obstacle(index_to_position(i)))
        obstacles.append(Obstacle(
            index_to_position(i+((GAME_INSTANCE_WIDTH//TILE_LEN)
                              * ((GAME_INSTANCE_HEIGHT//TILE_LEN)-1)))
        ))

    for i in range((GAME_INSTANCE_HEIGHT//TILE_LEN)):
        obstacles.append(
            Obstacle(index_to_position(
                i*(GAME_INSTANCE_WIDTH//TILE_LEN))
            ))
        obstacles.append(
            Obstacle(index_to_position(
                i*(GAME_INSTANCE_WIDTH//TILE_LEN) +
                (GAME_INSTANCE_WIDTH//TILE_LEN)-1
            )))

    return obstacles


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

    # Bend
    UP_LEFT = 4
    UP_RIGHT = 5
    DOWN_LEFT = 6
    DOWN_RIGHT = 7

    # Collision
    COLLIDED = 8
    COL_UP_LEFT = 9
    COL_UP_RIGHT = 10
    COL_DOWN_LEFT = 11
    COL_DOWN_RIGHT = 12
