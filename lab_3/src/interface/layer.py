from typing import Tuple, Any, Optional, List
from abc import ABC, abstractmethod
import pygame
from pygame.sprite import Group

from src.factories.bird_factory import ChickenFactory, SittingChickenFactory, FlyingChickenFactory, \
    HorizontalFlyingChickenFactory, RunningChickenFactory
from src.objects.balloon import Balloon
from src.objects.base_sprite import BaseObjectInLayer
from src.objects.chicken import HorizontalRunningChicken
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

    def clear(self)->None:
        self._group.empty()
        self._objects.empty()

    @property
    def speed(self)->int:
        return self._speed

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


class GameLayer(Layer):
    def __init__(self, image: pygame.Surface, name: str, layer_speed, y_range: Tuple[int, int]):
        super().__init__(image, name, layer_speed, y_range)
        self._factory_sitting = SittingChickenFactory(self._group)

    def create_chickens(self, count: int)->None:
        for _ in range(count):
            chicken = self._factory_sitting.create(self._y_range[0], self._y_range[1], self._speed, self._objects)
            if chicken:
                self._group.add(chicken)


class FieldLayer(Layer):
    def __init__(self, image: pygame.Surface, name: str, layer_speed, y_range: Tuple[int, int]):
        super().__init__(image, name, layer_speed, y_range)
        self._factory_flying = HorizontalFlyingChickenFactory(self._group)
        self._factory_running = RunningChickenFactory(self._group)

    def create_chickens(self, counts: Tuple[int, int]) -> None:
        running_count, flying_count = counts
        factories = (self._factory_running, self._factory_flying)

        for factory, count in zip(factories, (running_count, flying_count)):
            for _ in range(count):
                chicken = factory.create(self._y_range[0],self._y_range[1], self._speed, self._objects)
                if chicken:
                    self._group.add(chicken)
