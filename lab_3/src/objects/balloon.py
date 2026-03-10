import pygame

from src.objects.base_sprite import BaseSprite, BaseObjectInLayer
from src.settings.settings import BALLOON_IMAGE, BALLOON_SHOOT, BALLOON_DEAD_IMAGE, ALPHA, BLOOR_BALLOON_Y, \
    DELTA_FALLING_SPEED, FALLING_SPEED, SCORE_BALLOON


class Balloon(BaseObjectInLayer):
    def __init__(self, x: int, y: int, layer_speed: float) -> None:
        image = pygame.image.load(BALLOON_IMAGE).convert_alpha()
        super().__init__(image, x, y, layer_speed, SCORE_BALLOON)

        self._is_falling = False
        self._fall_speed = 0.0
        self._alpha = ALPHA

    def shoot(self) -> None:
        if not self._is_killed:
            self._is_killed = True
            self._is_falling = True
            self._fall_speed = FALLING_SPEED

    def animate(self) -> None:
        if not self._is_falling:
            return

        self._fall_speed += DELTA_FALLING_SPEED
        self.rect.y += self._fall_speed

        if self.rect.y > BLOOR_BALLOON_Y:
            self._alpha = max(0, self._alpha - 15)
            self.image.set_alpha(self._alpha)

        if self._alpha <= 0:
            self.kill()
            self._is_falling = False

    def play(self, volume: float) -> None:
        if not self._is_killed:
            self._player.set_sound(BALLOON_SHOOT)
            super().play(volume)