import random

import pygame
from abc import ABC, abstractmethod

from src.interface.cartridge import Cartridge
from src.settings.settings import BASE_WIDTH_OF_SITTING_CHICKEN, SCREEN_WIDTH, HEIGHT_FLYING_CHICKEN, SCREEN_HEIGHT, \
    FIRST_LAYER_HEIGHT, MIN_CHICKEN_SPEED, MAX_CHICKEN_SPEED, DEFAULT_SPEED_WORLD, COUNT_OF_ATTEMPTS_TO_CREATE_CHICKEN
from src.objects.chicken import SittingChicken, FlyingChicken, HorizontalFlyingChicken, HorizontalRunningChicken


class ChickenFactory(ABC):
    def __init__(self, all_birds: pygame.sprite.Group):
        self.all_birds = all_birds

    @abstractmethod
    def create(self, min_y, max_y, layer_speed,layer_objects:pygame.sprite.Group):
        pass


class SittingChickenFactory(ChickenFactory):
    def create(self, min_y: int, max_y: int, layer_speed: float, layer_objects:pygame.sprite.Group):
        x = random.randint(BASE_WIDTH_OF_SITTING_CHICKEN, 2*SCREEN_WIDTH - BASE_WIDTH_OF_SITTING_CHICKEN)
        y = random.randint(min_y, max_y)
        temp_bird = SittingChicken(x, y, layer_speed)
        if not pygame.sprite.spritecollide(temp_bird, self.all_birds, False) and not pygame.sprite.spritecollide(temp_bird, layer_objects, False):
            return temp_bird
        return None

class MoveChickenFactory(ChickenFactory):
    @abstractmethod
    def create_bird(self, x: int, y: int, layer_speed: float, speed: float, direction: str, min_y: int, max_y: int):
        pass

    def create(self, min_y: int, max_y: int, layer_speed: float, layer_objects: pygame.sprite.Group):
        for _ in range(COUNT_OF_ATTEMPTS_TO_CREATE_CHICKEN):
            direction = random.choice(["left", "right"])
            x = random.randint(-300, -1) if direction == "right" else random.randint(3 * SCREEN_WIDTH + 1,
                                                                                     3 * SCREEN_WIDTH + 300)
            y = random.randint(min_y, max_y)
            speed = random.uniform(MIN_CHICKEN_SPEED, MAX_CHICKEN_SPEED)
            temp_bird = self.create_bird(x, y, layer_speed, speed, direction, min_y, max_y)
            if not pygame.sprite.spritecollide(temp_bird, self.all_birds, False) and not pygame.sprite.spritecollide(
                    temp_bird, layer_objects, False):
                return temp_bird
        return None


class FlyingChickenFactory(MoveChickenFactory):
    def create_bird(self, x, y, layer_speed, speed, direction, min_y, max_y):
        return FlyingChicken(x, y, layer_speed, speed, direction, min_y, max_y)


class HorizontalFlyingChickenFactory(MoveChickenFactory):
    def create_bird(self, x, y, layer_speed, speed, direction, min_y, max_y):
        return HorizontalFlyingChicken(x, y, layer_speed, speed, direction)


class RunningChickenFactory(MoveChickenFactory):
    def create_bird(self, x, y, layer_speed, speed, direction, min_y, max_y):
        return HorizontalRunningChicken(x, y, layer_speed, speed, direction)

