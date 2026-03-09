import pygame

from src.settings.settings import HEDGEHOG_IMAGE, HEDGEHOG_AFTER_SHOOT_IMAGE, HEDGEHOG_COORD_X, HEDGEHOG_COORD_Y, \
    HEDGEHOG_SHOOT
from src.objects.base_sprite import BaseSprite, BaseObjectInLayer


class Hedgehog(BaseObjectInLayer):
    def __init__(self, x:int, y:int, layer_speed:float) -> None:
        image = pygame.image.load(HEDGEHOG_IMAGE).convert_alpha()
        super().__init__(image, x, y, layer_speed)

    def animate(self) -> None:
        if self._is_killed:
            self.image = pygame.image.load(HEDGEHOG_AFTER_SHOOT_IMAGE).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.x = HEDGEHOG_COORD_X
            self.rect.y = HEDGEHOG_COORD_Y

    def play(self, volume:float) -> None:
        if not self._is_killed:
            self._player.set_sound(HEDGEHOG_SHOOT)
            super().play(volume)