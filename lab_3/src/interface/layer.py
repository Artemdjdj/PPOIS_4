from typing import Tuple, Any
from abc import ABC, abstractmethod
import pygame

from src.factories.bird_factory import ChickenFactory, SittingChickenFactory, FlyingChickenFactory
from src.settings.settings import DEFAULT_SPEED_WORLD


class Layer(ABC):
    def __init__(self, image: pygame.Surface, name:str, layer_speed, y_range:Tuple[int, int]) -> None:
        self._image = image
        self._name = name
        self._speed = layer_speed
        self._y_range = y_range
        self._width = self._image.get_width()

    @abstractmethod
    def create_chickens(self, count: int)->None:
        pass

    def draw(self, screen, x, scroll_position) -> None:
        screen.blit(self._image, ((x * self._width) - scroll_position * self._speed, 0))

class SkyLayer(Layer):
    def __init__(self, image: pygame.Surface, name:str, layer_speed, y_range:Tuple[int, int],default_speed_chicken:float):
        self._default_speed = default_speed_chicken
        self._group = pygame.sprite.Group()
        self._factory = FlyingChickenFactory(self._group)
        super().__init__(image, name, layer_speed, y_range)

    def create_chickens(self, count: int)->None:
        for _ in range(count):
            chicken = self._factory.create(self._y_range[0], self._y_range[1], self._default_speed)
            if chicken:
                self._group.add(chicken)

    @property
    def chickens(self):
        return self._group

class GroundField(Layer):
    def __init__(self, image: pygame.Surface, name:str, layer_speed, y_range:Tuple[int, int]):
        self._group = pygame.sprite.Group()
        self._factory = SittingChickenFactory(self._group)
        super().__init__(image, name, layer_speed, y_range)

    def create_chickens(self, count: int)->None:
        for _ in range(count):
            chicken = self._factory.create(self._y_range[0], self._y_range[1], self._speed)
            if chicken:
                self._group.add(chicken)

    @property
    def chickens(self):
        return self._group

class FieldLayer(GroundField):
    def __init__(self, image: pygame.Surface, name:str, layer_speed, y_range:Tuple[int, int]):
        self._toilet = None
        super().__init__(image, name, layer_speed, y_range)


class GameLayer(GroundField):
    def __init__(self, image: pygame.Surface, name:str, layer_speed, y_range:Tuple[int, int]):
        self._car = None
        super().__init__(image, name, layer_speed, y_range)

