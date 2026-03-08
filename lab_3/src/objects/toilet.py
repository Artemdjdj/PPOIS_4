import pygame

from src.settings.settings import CAR_IMAGE, TOILET_IMAGE
from src.objects.base_sprite import BaseSprite, BaseObjectInLayer


class Toilet(BaseObjectInLayer):
    def __init__(self, x:int, y:int, layer_speed:float) -> None:
        image = pygame.image.load(TOILET_IMAGE).convert_alpha()
        super().__init__(image, x, y, layer_speed)
