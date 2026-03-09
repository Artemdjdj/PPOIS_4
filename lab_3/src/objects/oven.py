import time

import pygame

from src.settings.settings import OVEN_WITH_CHICKEN, OVEN_IMAGE, OVEN_COORD_X, OVEN_COORD_Y, TIME_AFTER_SHOOT, \
    OVEN_SHOOT
from src.objects.base_sprite import BaseSprite, BaseObjectInLayer


class Oven(BaseObjectInLayer):
    def __init__(self, x: int, y: int, layer_speed: float) -> None:
        self._img_with_chicken = pygame.image.load(OVEN_WITH_CHICKEN).convert_alpha()
        self._img_empty = pygame.image.load(OVEN_IMAGE).convert_alpha()
        self.shoot_time = None
        super().__init__(self._img_with_chicken, x, y, layer_speed)

    def shoot(self) -> None:
        self.shoot_time = time.time()
        super().shoot()

    def animate(self) -> None:
        if self._is_killed:
            current_time = time.time()
            x,y = self.rect.x, self.rect.y
            if self.shoot_time is not None and current_time - self.shoot_time >= TIME_AFTER_SHOOT:
                self.image = self._img_with_chicken
                self._is_killed = False
            else:
                self.image = self._img_empty
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    def play(self, volume:float) -> None:
        self._player.set_sound(OVEN_SHOOT)
        super().play(volume)