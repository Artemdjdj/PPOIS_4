import pygame

from src.objects.base_sprite import BaseObjectInLayer
from src.settings.settings import CARTRIDGE_IMAGE, SPACE_BETWEEN_CARTRIDGES


class Cartridge(BaseObjectInLayer):
    def __init__(self, x: int, y: int, layer_speed: float) -> None:
        image = pygame.image.load(CARTRIDGE_IMAGE).convert_alpha()
        super().__init__(image, x, y, layer_speed, None)
