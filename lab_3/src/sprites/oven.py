import pygame

from src.settings.settings import OVEN_WITH_CHICKEN
from src.sprites.base_sprite import BaseSprite


class Oven(BaseSprite):
    def __init__(self, x:int, y:int, layer_speed:float) -> None:
        image = pygame.image.load(OVEN_WITH_CHICKEN).convert_alpha()
        self.layer_speed = layer_speed
        super().__init__(image, x, y)

    def draw(self, screen: pygame.Surface, scroll_position: float) -> None:
        screen_x = self.rect.x - scroll_position * self.layer_speed
        screen.blit(self.image, (screen_x, self.rect.y))