import pygame

from src.objects.base_sprite import BaseSprite, BaseObjectInLayer
from src.settings.settings import BALLOON_IMAGE


class Balloon(BaseObjectInLayer):
    def __init__(self, x:int, y:int, layer_speed:float) -> None:
        image = pygame.image.load(BALLOON_IMAGE).convert_alpha()
        super().__init__(image, x, y, layer_speed)