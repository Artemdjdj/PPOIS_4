import pygame

from src.settings.settings import CAR_IMAGE, TOILET_IMAGE, DESTROYED_TOILET_IMAGE, TOILET_SHOOT
from src.objects.base_sprite import BaseSprite, BaseObjectInLayer


class Toilet(BaseObjectInLayer):
    def __init__(self, x:int, y:int, layer_speed:float) -> None:
        self._image_toilet = pygame.image.load(TOILET_IMAGE).convert_alpha()
        self._image_destroyed_toilet = pygame.image.load(DESTROYED_TOILET_IMAGE).convert_alpha()
        super().__init__(self._image_toilet, x, y, layer_speed)

    def animate(self) -> None:
        if self._is_killed:
            x,y = self.rect.x, self.rect.y
            self.image = self._image_destroyed_toilet
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    def play(self, volume:float) -> None:
        self._player.set_sound(TOILET_SHOOT)
        super().play(volume)