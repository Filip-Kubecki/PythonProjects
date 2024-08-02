import pygame
from tools import Direction


class Snake():
    def __init__(self, x, y):
        self.segments = list()
        self.segments.append(Segment(x, y))
        # self.segments.append(Segment(x, y+20))
        # self.add_segment()

    def self_collision(self):
        head = self.segments[0]
        for segment in self.segments[1:]:
            if head.rect.colliderect(segment.rect):
                # self.segments[0].color = "#db4949"
                return True
        return False

    def change_direction(self, new_direction):
        if not (self.segments[0].direction is Direction.UP and new_direction is Direction.DOWN or self.segments[0].direction is Direction.DOWN and new_direction is Direction.UP or
                self.segments[0].direction is Direction.RIGHT and new_direction is Direction.LEFT or
                self.segments[0].direction is Direction.LEFT and new_direction is Direction.RIGHT):
            self.segments[0].direction = new_direction

    def draw_snake(self, screen):
        for segment in self.segments:
            segment.draw_segment(screen)

    def update(self, screen):
        self.self_collision()
        for segment in self.segments:
            match segment.direction:
                case Direction.UP:
                    if segment.rect.y <= 0:
                        segment.rect.y = screen.get_height()-20 else:
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
            self.segments[i].direction = self.segments[i-1].direction

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

        new_segment.direction = tail.direction
        self.segments.append(new_segment)

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
        self.color = "#77b875"
        self.rect = pygame.rect.Rect(x, y, 20, 20)

    def draw_segment(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def change_direction(self, new_direction):
        self.direction = new_direction
