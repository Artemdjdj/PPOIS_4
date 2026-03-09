import pygame

from src.interface.sound_player import SoundPlayer
from src.settings.settings import SCREEN_WIDTH
from src.utils.image_formatter import ImageFormatter


class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface,x: int, y: int) -> None:
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self._is_killed = False

    def shoot(self)->None:
        self._is_killed = True

    def animate(self) -> None:
        pass


class BaseObjectInLayer(BaseSprite):
    def __init__(self, image: pygame.Surface,x:int, y:int, layer_speed:float,) -> None:
        self.layer_speed = layer_speed
        self._player = SoundPlayer()
        super().__init__(image, x, y)

    def draw(self, screen: pygame.Surface, scroll_position: float) -> None:
        screen_x = self.rect.x - scroll_position * self.layer_speed
        screen.blit(self.image, (screen_x, self.rect.y))

    def play(self, volume)->None:
        if self._player:
            self._player.play(volume)

