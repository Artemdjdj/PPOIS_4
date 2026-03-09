import pygame

from src.settings.settings import CAR_IMAGE, CAR_SHOOT
from src.objects.base_sprite import BaseSprite, BaseObjectInLayer


class Car(BaseObjectInLayer):
    def __init__(self, x:int, y:int, layer_speed:float) -> None:
        image = pygame.image.load(CAR_IMAGE).convert_alpha()
        super().__init__(image, x, y, layer_speed)

    def animate(self) -> None:
        self.image = pygame.image.load(CAR_IMAGE).convert_alpha()

    def play(self, volume:float) -> None:
        self._player.set_sound(CAR_SHOOT)
        super().play(volume)