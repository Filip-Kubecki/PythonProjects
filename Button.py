import pygame
from resources import Style
import tools
from config import *


class Button(pygame.Surface):
    def __init__(self, width, height, position, icon_src=None, text=None, font=None):
        super().__init__((width, height), pygame.SRCALPHA)
        self.position = position

        self.fill(Style.LIGHT_GREEN)

        self._rect_background = pygame.Surface(
            (width, height), pygame.SRCALPHA)
        self._rect_background.set_alpha(0)
        self._rect_background.fill(Style.CREAMY_WHITE)

        self._font = font
        self._text = text

        self._icon = pygame.image.load(
            icon_src) if icon_src is not None else None

    def display(self, screen):
        self.fill(Style.LIGHT_GREEN)
        if self._text is not None and self._font is not None:
            self._font.render_to(
                self,
                ((self.get_width() // 2) - (self._font.get_rect(self._text).width // 2),
                 (self.get_height() // 2) -
                 (self._font.get_rect(self._text).height // 2)),
                self._text,
                "Black"
            )

        if self._icon is not None:
            img_len = PAUSE_SCREEN_IMG_REAL_SIZE
            img_offset = (self.get_width()/2)-(img_len/2)
            self.blit(self._icon, (img_offset, img_offset))

        self.blit(self._rect_background, (0, 0))
        screen.blit(self, self.position)

    def mouse_click(self):
        if (pygame.mouse.get_pressed()[0] and
                tools.check_if_mouse_collide(pygame.mouse.get_pos(), self.position, self.get_size())):
            return True
        return False

    def hover(self):
        if tools.check_if_mouse_collide(pygame.mouse.get_pos(), self.position, self.get_size()):
            self._rect_background.set_alpha(40)
        else:
            self._rect_background.set_alpha(0)
