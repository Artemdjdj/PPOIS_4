import pygame

from src.settings.settings import CAR_IMAGE, TOILET_IMAGE, DESTROYED_TOILET_IMAGE, TOILET_SHOOT, NOT_TOILET_IMAGE
from src.objects.base_sprite import BaseSprite, BaseObjectInLayer


class Toilet(BaseObjectInLayer):
    def __init__(self, x:int, y:int, layer_speed:float) -> None:
        self._image_toilet = pygame.image.load(TOILET_IMAGE).convert_alpha()
        self._image_destroyed_toilet = pygame.image.load(DESTROYED_TOILET_IMAGE).convert_alpha()
        self._image_not_toilet = pygame.image.load(NOT_TOILET_IMAGE).convert_alpha()
        self._count_of_shoots = 0
        self._is_toilet_nothing = False
        score = -5
        super().__init__(self._image_toilet, x, y, layer_speed, score)

    def shoot(self)->None:
        self._count_of_shoots += 1

        if self._count_of_shoots >3:
            self._is_killed = True

        if self._count_of_shoots>9:
            self.score = None
            self._is_toilet_nothing = True

    def animate(self) -> None:
        if self._is_killed or self._image_not_toilet:
            x, y = self.rect.x, self.rect.y
            if self._is_killed and not self._is_toilet_nothing:
                self.image = self._image_destroyed_toilet
            elif self._is_toilet_nothing:
                self.image = self._image_not_toilet
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    def play(self, volume:float) -> None:
        if not self._is_toilet_nothing:
            self._player.set_sound(TOILET_SHOOT)
            super().play(volume)