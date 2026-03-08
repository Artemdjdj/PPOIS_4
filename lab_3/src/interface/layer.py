from typing import Tuple, Any, Optional, List
from abc import ABC, abstractmethod
import pygame
from pygame.sprite import Group

from src.factories.bird_factory import ChickenFactory, SittingChickenFactory, FlyingChickenFactory
from src.objects.balloon import Balloon
from src.objects.base_sprite import BaseObjectInLayer
from src.objects.toilet import Toilet
from src.settings.settings import DEFAULT_SPEED_WORLD
from src.objects.car import Car
from src.objects.oven import Oven


class Layer(ABC):
    def __init__(self, image: pygame.Surface, name:str, layer_speed, y_range:Tuple[int, int]) -> None:
        self._image = image
        self._name = name
        self._speed = layer_speed
        self._y_range = y_range
        self._width = self._image.get_width()
        self._group = pygame.sprite.Group()
        self._objects = pygame.sprite.Group()

    def add_object(self, new_element:BaseObjectInLayer)->None:
        if not pygame.sprite.spritecollide(new_element, self._objects, False):
            self._objects.add(new_element)

    @property
    def objects(self) -> pygame.sprite.Group:
        return self._objects

    @property
    def chickens(self):
        return self._group

    @abstractmethod
    def create_chickens(self, count: int)->None:
        pass

    def draw(self, screen, x, scroll_position) -> None:
        screen.blit(self._image, ((x * self._width) - scroll_position * self._speed, 0))

class SkyLayer(Layer):
    def __init__(self, image: pygame.Surface, name:str, layer_speed, y_range:Tuple[int, int],default_speed_chicken:float):
        self._default_speed = default_speed_chicken
        super().__init__(image, name, layer_speed, y_range)
        self._factory = FlyingChickenFactory(self._group)

    def create_chickens(self, count: int)->None:
        for _ in range(count):
            chicken = self._factory.create(self._y_range[0], self._y_range[1], self._default_speed, self._objects)
            if chicken:
                self._group.add(chicken)

class GroundField(Layer):
    def __init__(self, image: pygame.Surface, name:str, layer_speed, y_range:Tuple[int, int]):
        super().__init__(image, name, layer_speed, y_range)
        self._factory = SittingChickenFactory(self._group)

    def create_chickens(self, count: int)->None:
        for _ in range(count):
            chicken = self._factory.create(self._y_range[0], self._y_range[1], self._speed, self._objects)
            if chicken:
                self._group.add(chicken)

class FieldLayer(GroundField):
    def __init__(self, image: pygame.Surface, name:str, layer_speed, y_range:Tuple[int, int]):
        super().__init__(image, name, layer_speed, y_range)

class GameLayer(GroundField):
    def __init__(self, image: pygame.Surface, name:str, layer_speed, y_range:Tuple[int, int]):
        super().__init__(image, name, layer_speed, y_range)
