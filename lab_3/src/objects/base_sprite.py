import pygame

from src.settings.settings import SCREEN_WIDTH
from src.utils.image_formatter import ImageFormatter


class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface,x: int, y: int) -> None:
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
