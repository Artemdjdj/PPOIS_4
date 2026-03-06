import pygame

from src.settings.settings import SCREEN_WIDTH
from src.utils.image_formatter import ImageFormatter


class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, image: str,x: int, y: int) -> None:
        super().__init__()
        self._image = ImageFormatter.scale_image(pygame.image.load(image).convert_alpha(), 90)
        self._rect = self._image.get_rect()
        self._rect.x = x
        self._rect.y = y
