from typing import Tuple, Any, Optional, List
from abc import ABC, abstractmethod
import pygame

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
        self._objects = []

    def add_object(self, new_element:BaseObjectInLayer)->None:
        self._objects.append(new_element)

    @property
    def objects(self) -> List[BaseObjectInLayer]:
        return self._objects

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
        # self._ballon = None
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
        # self._toilet = None
        super().__init__(image, name, layer_speed, y_range)

    # @property
    # def toilet(self) -> Optional[Toilet]:
    #     return self._toilet
    #
    # @toilet.setter
    # def toilet(self, toilet:Toilet):
    #     self._toilet = toilet

class GameLayer(GroundField):
    def __init__(self, image: pygame.Surface, name:str, layer_speed, y_range:Tuple[int, int]):
        # self._car = None
        # self._oven = None
        # self._static_objects = []
        super().__init__(image, name, layer_speed, y_range)

    # @property
    # def car(self)->Optional[Car]:
    #     return self._car
    #
    # @car.setter
    # def car(self, car: Car):
    #     self._car = car
    #
    # @property
    # def oven(self)->Optional[Oven]:
    #     return self._oven
    #
    # @oven.setter
    # def oven(self, oven:Oven)->None:
    #     self._oven = oven
