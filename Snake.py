import pygame
import Textures_src
import config
import tools
from tools import Direction
from tools import Snake_texture_state


class Snake():
    def __init__(self, x, y):
        self.segments = list()
        self.current_direction = Direction.NONE

        next_segment_y = config.TILE_LEN

        # Setting up head
        self.segments.append(Segment(x, y))
        self.segments[0].texture_state = Snake_texture_state.HEAD
        self.segments[0].change_texture()

        # Setting up initial segments - right now one
        for i in range(config.SNAKE_SEGMENT_NUMBER - 2):
            new_segment = Segment(x, y+next_segment_y)
            next_segment_y += config.TILE_LEN
            new_segment.direction = Direction.UP
            new_segment.texture_state = Snake_texture_state.SEGMENT
            new_segment.change_texture()
            self.segments.append(new_segment)

        # Setting up tail
        tail = Segment(x, y+next_segment_y)
        tail.direction = Direction.UP
        self.segments.append(tail)

    def self_collision(self, screen):
        head = self.segments[0]
        for segment in self.segments[1:]:
            if head.rect.colliderect(segment.rect):
                self.decapitate(screen)
                return True
        return False

    def decapitate(self, screen):
        self.segments.pop(0)

        head = self.segments[0]
        head_direction = head.direction
        prev_direction = self.segments[1].direction

        match head_direction:
            case Direction.UP:
                match prev_direction:
                    case Direction.LEFT:
                        head.texture_state = Snake_texture_state.COL_UP_RIGHT
                        head.change_texture()
                        head.rotate_img(90.0)
                    case Direction.RIGHT:
                        head.texture_state = Snake_texture_state.COL_UP_LEFT
                        head.change_texture()
                        head.rotate_img(-90.0)
            case Direction.DOWN:
                match prev_direction:
                    case Direction.LEFT:
                        head.texture_state = Snake_texture_state.COL_UP_LEFT
                        head.change_texture()
                        head.rotate_img(90.0)
                    case Direction.RIGHT:
                        head.texture_state = Snake_texture_state.COL_UP_RIGHT
                        head.change_texture()
                        head.rotate_img(-90.0)
            case Direction.LEFT:
                match prev_direction:
                    case Direction.UP:
                        head.texture_state = Snake_texture_state.COL_UP_LEFT
                        head.change_texture()
                    case Direction.DOWN:
                        head.texture_state = Snake_texture_state.COL_UP_RIGHT
                        head.change_texture()
                        head.rotate_img(180.0)
            case Direction.RIGHT:
                match prev_direction:
                    case Direction.UP:
                        head.texture_state = Snake_texture_state.COL_UP_RIGHT
                        head.change_texture()
                    case Direction.DOWN:
                        head.texture_state = Snake_texture_state.COL_UP_LEFT
                        head.change_texture()
                        head.rotate_img(180.0)

        if head_direction == prev_direction:
            head.texture_state = Snake_texture_state.COLLIDED
            head.change_texture()
            head.rotate_texture()

        head.draw_segment(screen)
        self.segments[0] = head

    def change_direction(self, new_direction):
        # Protecting user from turning snake head in the direction of its body
        if not (self.current_direction is Direction.UP and new_direction is Direction.DOWN or
                self.current_direction is Direction.DOWN and new_direction is Direction.UP or
                self.current_direction is Direction.RIGHT and new_direction is Direction.LEFT or
                self.current_direction is Direction.LEFT and new_direction is Direction.RIGHT):
            self.segments[0].direction = new_direction

    def draw_snake(self, screen):
        for segment in self.segments:
            segment.draw_segment(screen)

    def update(self, screen):
        self.current_direction = self.segments[0].direction

        for segment in self.segments:
            match segment.direction:
                case Direction.UP:
                    if segment.rect.y <= 0 and not config.GAME_INSTANCE_BORDER_COLLISION:
                        segment.rect.y = screen.get_height()-config.TILE_LEN
                    elif segment.rect.y <= 0:
                        self.self_collision(screen)
                    else:
                        segment.rect.y -= config.TILE_LEN
                case Direction.DOWN:
                    if (segment.rect.y >= screen.get_height()-config.TILE_LEN and
                            not config.GAME_INSTANCE_BORDER_COLLISION):
                        segment.rect.y = 0
                    elif (segment.rect.y >= screen.get_height()-config.TILE_LEN):
                        self.self_collision(screen)
                    else:
                        segment.rect.y += config.TILE_LEN
                case Direction.LEFT:
                    if segment.rect.x <= 0 and not config.GAME_INSTANCE_BORDER_COLLISION:
                        segment.rect.x = screen.get_width()-config.TILE_LEN
                    elif segment.rect.x <= 0:
                        self.self_collision(screen)
                    else:
                        segment.rect.x -= config.TILE_LEN
                case Direction.RIGHT:
                    if (segment.rect.x >= screen.get_width()-config.TILE_LEN and
                            not config.GAME_INSTANCE_BORDER_COLLISION):
                        segment.rect.x = 0
                    elif segment.rect.x >= screen.get_width()-config.TILE_LEN:
                        self.self_collision(screen)
                    else:
                        segment.rect.x += config.TILE_LEN

        self.update_direction()

    def update_direction(self):
        # Rotating HEAD texture without changing directino - direction set to current direction
        self.segments[0].change_direction(self.segments[0].direction)

        # Iterate over segments excluding HEAD - rever iteration
        if len(self.segments) > 1:
            for i in range(len(self.segments)-1, 0, -1):
                # Set segment texture to SEGMENT if current segment isn't a tail
                if i != len(self.segments)-1:
                    self.segments[i].texture_state = Snake_texture_state.SEGMENT

                if self.segments[i].texture_state is not Snake_texture_state.TAIL:
                    # Change texture for bended segments
                    self.segments[i].change_texture_according_to_prev_direction(
                        self.segments[i-1].direction)

                # Change current segment direction to direction of previouse segment direction
                self.segments[i].change_direction(self.segments[i-1].direction)

    def add_segment(self, screen):
        tail = self.segments[-1]

        new_segment = Segment(tail.rect.x, tail.rect.y)

        match tail.direction:
            case Direction.UP:
                new_segment.rect.y += config.TILE_LEN
            case Direction.DOWN:
                new_segment.rect.y -= config.TILE_LEN
            case Direction.LEFT:
                new_segment.rect.x += config.TILE_LEN
            case Direction.RIGHT:
                new_segment.rect.x -= config.TILE_LEN

        new_segment.texture_state = Snake_texture_state.TAIL
        new_segment.direction = tail.direction
        new_segment.change_direction(tail.direction)
        self.segments.append(new_segment)

        # new_segment.direction = tail.direction
        if len(self.segments) > 2:
            self.segments[-2].texture_state = Snake_texture_state.SEGMENT
            self.segments[-2].change_texture()
            self.segments[-2].rotate_texture()

    def key_event(self, key_event):
        if key_event[pygame.K_w]:
            self.change_direction(Direction.UP)
        elif key_event[pygame.K_s]:
            self.change_direction(Direction.DOWN)
        elif key_event[pygame.K_a]:
            self.change_direction(Direction.LEFT)
        elif key_event[pygame.K_d]:
            self.change_direction(Direction.RIGHT)

    def get_position_indexes(self):
        indexes = list()
        for segment in self.segments:
            position = (segment.rect.x, segment.rect.y)
            indexes.append(tools.position_to_index(position))
        return indexes


class Segment():
    def __init__(self, x, y):
        self.direction = Direction.UP
        self.rect = pygame.rect.Rect(x, y, config.TILE_LEN, config.TILE_LEN)
        self.img = pygame.image.load(Textures_src.SNAKE_TAIL)
        self.scale = 1
        if (config.TILE_LEN > 20):
            self.scale = config.TILE_LEN // 20
            self.img = pygame.transform.scale_by(self.img, self.scale)
        self.angle = 0.0
        self.texture_state = Snake_texture_state.TAIL

    def draw_segment(self, screen):
        screen.blit(self.img, (self.rect.x, self.rect.y))

    def change_direction(self, new_direction):
        self.direction = new_direction

        # Resets angle of the texture 0 degree
        self.img = pygame.transform.rotate(self.img, 360.0 - self.angle)
        self.change_texture()

        if (self.texture_state is Snake_texture_state.TAIL or
            self.texture_state is Snake_texture_state.HEAD or
            self.texture_state is Snake_texture_state.COLLIDED or
                self.texture_state is Snake_texture_state.SEGMENT):
            self.rotate_texture()

    def rotate_img(self, angle):
        self.img = pygame.transform.rotate(self.img, angle)

    def rotate_texture(self):
        # Rotates texture to the direction of movement
        match self.direction:
            case Direction.UP:
                self.img = pygame.transform.rotate(self.img, 0)
                self.angle = 0.0
            case Direction.DOWN:
                self.img = pygame.transform.rotate(self.img, 180)
                self.angle = 180
            case Direction.LEFT:
                self.img = pygame.transform.rotate(self.img, 90)
                self.angle = 90
            case Direction.RIGHT:
                self.img = pygame.transform.rotate(self.img, 270)
                self.angle = 270

    def change_texture_according_to_prev_direction(self, prev_direction):
        match self.direction:
            case Direction.UP:
                if prev_direction is Direction.LEFT:
                    self.texture_state = Snake_texture_state.UP_LEFT
                elif prev_direction is Direction.RIGHT:
                    self.texture_state = Snake_texture_state.UP_RIGHT
            case Direction.DOWN:
                if prev_direction is Direction.LEFT:
                    self.texture_state = Snake_texture_state.DOWN_LEFT
                elif prev_direction is Direction.RIGHT:
                    self.texture_state = Snake_texture_state.DOWN_RIGHT
            case Direction.LEFT:
                if prev_direction is Direction.DOWN:
                    self.texture_state = Snake_texture_state.UP_RIGHT
                elif prev_direction is Direction.UP:
                    self.texture_state = Snake_texture_state.DOWN_RIGHT
            case Direction.RIGHT:
                if prev_direction is Direction.DOWN:
                    self.texture_state = Snake_texture_state.UP_LEFT
                elif prev_direction is Direction.UP:
                    self.texture_state = Snake_texture_state.DOWN_LEFT

    def change_texture(self):
        # Change texture based on Snake_texture_state - head, tail, segment etc
        match self.texture_state:
            case Snake_texture_state.HEAD:
                self.img = pygame.image.load(Textures_src.SNAKE_HEAD)
            case Snake_texture_state.TAIL:
                self.img = pygame.image.load(Textures_src.SNAKE_TAIL)
            case Snake_texture_state.SEGMENT:
                self.img = pygame.image.load(Textures_src.SNAKE_SEGMENT)
            case Snake_texture_state.DOWN_RIGHT:
                self.img = pygame.image.load(Textures_src.SNAKE_BEND)
                self.img = pygame.transform.rotate(self.img, 180.0)
                self.angle = 180.0
            case Snake_texture_state.DOWN_LEFT:
                self.img = pygame.image.load(Textures_src.SNAKE_BEND)
                self.img = pygame.transform.rotate(self.img, 270.0)
                self.angle = 270.0
            case Snake_texture_state.UP_RIGHT:
                self.img = pygame.image.load(Textures_src.SNAKE_BEND)
                self.img = pygame.transform.rotate(self.img, 90.0)
                self.angle = 90.0
            case Snake_texture_state.UP_LEFT:
                self.img = pygame.image.load(Textures_src.SNAKE_BEND)
            case Snake_texture_state.COLLIDED:
                self.img = pygame.image.load(Textures_src.SNAKE_COLLIDED)
            case Snake_texture_state.COL_UP_RIGHT:
                self.img = pygame.image.load(Textures_src.SNAKE_COLLIDED_RIGHT)
            case Snake_texture_state.COL_UP_LEFT:
                self.img = pygame.image.load(Textures_src.SNAKE_COLLIDED_LEFT)

        self.img = pygame.transform.scale_by(self.img, self.scale)
