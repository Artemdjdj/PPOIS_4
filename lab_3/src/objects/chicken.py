import random
import pygame
from src.settings.settings import SCREEN_WIDTH, SITTING_CHICKEN, HEIGHT_FLYING_CHICKEN, SCALE_IMAGE_THIRD_POWER, \
    SCALE_IMAGE_SECOND_POWER, BASE_WIDTH_OF_SITTING_CHICKEN, SCREEN_HEIGHT, SPEED_THIRD_LAYER, LEFT_FLYING_CHICKEN, \
    RIGHT_FLYING_CHICKEN, MIN_CHICKEN_SPEED, MAX_CHICKEN_SPEED, DEFAULT_SPEED_WORLD
from src.objects.base_sprite import BaseSprite
from src.utils.image_formatter import ImageFormatter


class BaseChicken(BaseSprite):
    def __init__(self, image: pygame.Surface, x: int, y: int, layer_speed: float) -> None:
        super().__init__(image, x, y)
        self.layer_speed = layer_speed

    def draw(self, screen: pygame.Surface, scroll_position: float) -> None:
        screen_x = self.rect.x - scroll_position * self.layer_speed
        screen.blit(self.image, (screen_x, self.rect.y))

    def update(self, dt:float) -> None:
        pass


class SittingChicken(BaseChicken):
    def __init__(self, x: int, y: int, layer_speed: float):
        scale = self._get_size(layer_speed)
        width = int(BASE_WIDTH_OF_SITTING_CHICKEN * scale)
        image = ImageFormatter.scale_image(
            pygame.image.load(SITTING_CHICKEN).convert_alpha(),
            width
        )
        super().__init__(image, x, y, layer_speed)

    @staticmethod
    def _get_size(layer_speed: float) -> float:
        if layer_speed == SPEED_THIRD_LAYER:
            return SCALE_IMAGE_THIRD_POWER
        return SCALE_IMAGE_SECOND_POWER


class FlyingChicken(BaseChicken):
    def __init__(self, x: int, y: int, layer_speed:float, velocity: float, direction: str):
        self._direction = direction
        self._velocity = velocity
        self._float_x = float(x)

        image_path = LEFT_FLYING_CHICKEN if direction == "left" else RIGHT_FLYING_CHICKEN
        image = pygame.image.load(image_path).convert_alpha()
        super().__init__(image, x, y, layer_speed)

    def update(self, dt:float) -> None:
        if self._direction == "left":
            self._float_x -= self._velocity * dt
        else:
            self._float_x += self._velocity * dt

        self.rect.x = int(self._float_x)

    def draw(self, screen: pygame.Surface, scroll_position: float) -> None:
        screen_x = self.rect.x - scroll_position * self.layer_speed
        screen.blit(self.image, (screen_x, self.rect.y))

