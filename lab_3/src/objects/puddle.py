import pygame

from src.settings.settings import PUDDLE_IMAGE, PUDDLE_SHOOT
from src.objects.base_sprite import BaseSprite, BaseObjectInLayer


class Puddle(BaseObjectInLayer):
    def __init__(self, x:int, y:int, layer_speed:float) -> None:
        image = pygame.image.load(PUDDLE_IMAGE).convert_alpha()
        super().__init__(image, x, y, layer_speed, -1)

    def play(self, volume:float) -> None:
        self._player.set_sound(PUDDLE_SHOOT)
        super().play(volume)