import pygame

from src.settings.settings import CAR_IMAGE, HEDGEHOG_IMAGE
from src.objects.base_sprite import BaseSprite, BaseObjectInLayer


class Hedgehog(BaseObjectInLayer):
    def __init__(self, x:int, y:int, layer_speed:float) -> None:
        image = pygame.image.load(HEDGEHOG_IMAGE).convert_alpha()
        super().__init__(image, x, y, layer_speed)
