import pygame
from tools import Direction
from tools import Snake_texture_state


class Snake():
    def __init__(self, x, y):
        self.segments = list()
        self.segments.append(Segment(x, y))
        self.segments[0].texture_state = Snake_texture_state.HEAD
        self.segments[0].change_texture()
        # self.segments.append(Segment(x, y+20))
        # self.add_segment()

    def self_collision(self):
        head = self.segments[0]
        for segment in self.segments[1:]:
            if head.rect.colliderect(segment.rect):
                return True
        return False

    def change_direction(self, new_direction):
        if not (self.segments[0].direction is Direction.UP and new_direction is Direction.DOWN or self.segments[0].direction is Direction.DOWN and new_direction is Direction.UP or
                self.segments[0].direction is Direction.RIGHT and new_direction is Direction.LEFT or
                self.segments[0].direction is Direction.LEFT and new_direction is Direction.RIGHT):
            self.segments[0].change_direction(new_direction)

    def draw_snake(self, screen):
        for segment in self.segments:
            segment.draw_segment(screen)

    def update(self, screen):
        self.self_collision()
        for segment in self.segments:
            match segment.direction:
                case Direction.UP:
                    if segment.rect.y <= 0:
                        segment.rect.y = screen.get_height()-20
                    else:
                        segment.rect.y -= 20
                case Direction.DOWN:
                    if segment.rect.y >= screen.get_height()-20:
                        segment.rect.y = 0
                    else:
                        segment.rect.y += 20
                case Direction.LEFT:
                    if segment.rect.x <= 0:
                        segment.rect.x = screen.get_width()-20
                    else:
                        segment.rect.x -= 20
                case Direction.RIGHT:
                    if segment.rect.x >= screen.get_width()-20:
                        segment.rect.x = 0
                    else:
                        segment.rect.x += 20
        self.update_direction()

    def update_direction(self):
        for i in range(len(self.segments)-1, 0, -1):
            if i != len(self.segments)-1:
                self.segments[i].texture_state = Snake_texture_state.SEGMENT
            self.segments[i].change_direction(self.segments[i-1].direction)

    def add_segment(self):
        tail = self.segments[-1]

        new_segment = Segment(tail.rect.x, tail.rect.y)

        match tail.direction:
            case Direction.UP:
                new_segment.rect.y += 20
            case Direction.DOWN:
                new_segment.rect.y -= 20
            case Direction.LEFT:
                new_segment.rect.x += 20
            case Direction.RIGHT:
                new_segment.rect.x -= 20

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


class Segment():
    def __init__(self, x, y):
        self.direction = Direction.NONE
        self.rect = pygame.rect.Rect(x, y, 20, 20)
        self.img = pygame.image.load(
            '/home/bork/PythonProjects/SnakeWithPyGame/img/snake_tail.png')
        self.angle = 0.0
        self.texture_state = Snake_texture_state.TAIL

    def draw_segment(self, screen):
        screen.blit(self.img, (self.rect.x, self.rect.y))

    def change_direction(self, new_direction):
        self.direction = new_direction
        self.img = pygame.transform.rotate(self.img, 360.0 - self.angle)
        self.change_texture()
        self.rotate_texture()

    def rotate_texture(self):
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

    def change_texture(self):
        # Change texture based on Snake_texture_state - head, tail, segment etc
        match self.texture_state:
            case Snake_texture_state.HEAD:
                self.img = pygame.image.load(
                    '/home/bork/PythonProjects/SnakeWithPyGame/img/snake_head.png')
            case Snake_texture_state.TAIL:
                self.img = pygame.image.load(
                    '/home/bork/PythonProjects/SnakeWithPyGame/img/snake_tail.png')
            case Snake_texture_state.SEGMENT:
                self.img = pygame.image.load(
                    '/home/bork/PythonProjects/SnakeWithPyGame/img/snake_streight.png')
