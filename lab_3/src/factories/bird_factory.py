import random

import pygame
from abc import ABC, abstractmethod

from src.settings.settings import BASE_WIDTH_OF_SITTING_CHICKEN, SCREEN_WIDTH, HEIGHT_FLYING_CHICKEN, SCREEN_HEIGHT
from src.sprites.chicken import SittingChicken


class ChickenFactory(ABC):
    def __init__(self, all_birds: pygame.sprite.Group):
        self.all_birds = all_birds

    @abstractmethod
    def create(self, min_y, max_y, layer_speed):
        pass


class SittingChickenFactory(ChickenFactory):
    def create(self, min_y: int, max_y: int, layer_speed: float):
        x = random.randint(BASE_WIDTH_OF_SITTING_CHICKEN, 2*SCREEN_WIDTH - BASE_WIDTH_OF_SITTING_CHICKEN)
        y = random.randint(min_y, max_y)
        temp_bird = SittingChicken(x, y, layer_speed)
        if not pygame.sprite.spritecollide(temp_bird, self.all_birds, False):
            return temp_bird
        return None