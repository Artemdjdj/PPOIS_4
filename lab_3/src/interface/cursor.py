import pygame

from src.settings.settings import CROSSHAIR_IMAGE


class Cursor:
    def __init__(self)->None:
        self._cursor_img = pygame.image.load(CROSSHAIR_IMAGE).convert_alpha()
        self._cursor_rect = self._cursor_img.get_rect()

    def draw(self, screen:pygame.Surface)->None:
        mouse_pos = pygame.mouse.get_pos()
        self._cursor_rect.center = mouse_pos
        screen.blit(self._cursor_img, self._cursor_rect)