import random

import pygame
from abc import ABC, abstractmethod

from src.interface.cartridge import Cartridge
from src.settings.settings import BASE_WIDTH_OF_SITTING_CHICKEN, SCREEN_WIDTH, HEIGHT_FLYING_CHICKEN, SCREEN_HEIGHT, \
    FIRST_LAYER_HEIGHT, MIN_CHICKEN_SPEED, MAX_CHICKEN_SPEED, DEFAULT_SPEED_WORLD
from src.objects.chicken import SittingChicken, FlyingChicken, HorizontalFlyingChicken


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


class FlyingChickenFactory(ChickenFactory):
    def create(self, min_y: int, max_y: int, layer_speed: float,layer_objects:pygame.sprite.Group):
        x = random.randint(-100, 3*SCREEN_WIDTH)
        y = random.randint(min_y, max_y)

        direction = random.choice(["left", "right"])
        speed = random.uniform(MIN_CHICKEN_SPEED, MAX_CHICKEN_SPEED)

        temp_bird = FlyingChicken(x, y,layer_speed, speed, direction, min_y, max_y)

        if not pygame.sprite.spritecollide(temp_bird, self.all_birds, False) and not pygame.sprite.spritecollide(temp_bird, layer_objects, False):
            return temp_bird

        return None


class HorizontalFlyingChickenFactory(ChickenFactory):
    def create(self, min_y: int, max_y: int, layer_speed: float, layer_objects:pygame.sprite.Group):
        x = random.randint(-100, 3*SCREEN_WIDTH)
        y = random.randint(min_y, max_y)

        direction = random.choice(["left", "right"])
        speed = random.uniform(MIN_CHICKEN_SPEED, MAX_CHICKEN_SPEED)

        temp_bird = HorizontalFlyingChicken(x, y,layer_speed, speed, direction)

        if not pygame.sprite.spritecollide(temp_bird, self.all_birds, False) and not pygame.sprite.spritecollide(temp_bird, layer_objects, False):
            return temp_bird

        return None


