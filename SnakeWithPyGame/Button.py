import pygame
import Style
import tools


class Button(pygame.Surface):
    def __init__(self, x, y, position, icon_src):
        super().__init__((x, y), pygame.SRCALPHA)
        self.position = position

        self.fill(Style.LIGHT_GREEN)
        self.set_alpha(255)

        self.icon = pygame.image.load(icon_src)
        self.blit(self.icon, (0, 0))

    def display(self, screen):
        screen.blit(self, self.position)

    def mouse_click(self):
        if (pygame.mouse.get_pressed()[0] and
                tools.check_if_mouse_collide(pygame.mouse.get_pos(), self.position, self.get_size())):
            return True
        return False

    def hover(self):
        if tools.check_if_mouse_collide(pygame.mouse.get_pos(), self.position, self.get_size()):
            self.set_alpha(100)
        else:
            self.set_alpha(255)
