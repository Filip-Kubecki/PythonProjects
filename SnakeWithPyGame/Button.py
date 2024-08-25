import pygame
import Style
import tools


class Button(pygame.Surface):
    def __init__(self, x, y, icon_src):
        super().__init__((x, y))
        self.position = (500, 20)

        self.fill(Style.CREAMY_WHITE)

        self.icon = pygame.image.load(icon_src)
        self.blit(self.icon, (0, 0))

    def display(self, screen):
        screen.blit(self, self.position)

    def mouse_click(self, func):
        if (pygame.mouse.get_pressed()[0] and
                tools.check_if_mouse_collide(pygame.mouse.get_pos(), self.position, self.get_size())):
            func()
