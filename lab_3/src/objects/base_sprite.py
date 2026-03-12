from typing import Optional

import pygame

from src.interface.sound_player import SoundPlayer
from src.settings.settings import SCREEN_WIDTH
from src.utils.image_formatter import ImageFormatter


class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface, x: int, y: int, score: Optional[int]) -> None:
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self._is_killed = False
        self._player = SoundPlayer()
        self.score: Optional[int] = score

    def shoot(self) -> None:
        self._is_killed = True

    def animate(self) -> None:
        pass

    def play(self, volume) -> None:
        if self._player:
            self._player.play(volume)


class BaseObjectInLayer(BaseSprite):
    def __init__(self, image: pygame.Surface, x: int, y: int, layer_speed: float, score: Optional[int]) -> None:
        self.layer_speed = layer_speed
        super().__init__(image, x, y, score)

    def draw(self, screen: pygame.Surface, scroll_position: float) -> None:
        screen_x = self.rect.x - scroll_position * self.layer_speed
        screen.blit(self.image, (screen_x, self.rect.y))
