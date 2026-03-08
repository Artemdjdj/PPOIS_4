import pygame

from src.objects.base_sprite import BaseSprite
from src.settings.settings import BALLOON_IMAGE


class Balloon(BaseSprite):
    def __init__(self, x:int, y:int, layer_speed:float) -> None:
        image = pygame.image.load(BALLOON_IMAGE).convert_alpha()
        self.layer_speed = layer_speed
        super().__init__(image, x, y)

    def draw(self, screen: pygame.Surface, scroll_position: float) -> None:
        screen_x = self.rect.x - scroll_position * self.layer_speed
        screen.blit(self.image, (screen_x, self.rect.y))