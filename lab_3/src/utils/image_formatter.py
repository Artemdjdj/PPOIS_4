import pygame
from pygame import Surface


class ImageFormatter:
    @staticmethod
    def scale_image(image: Surface, target_width: int):
        original_width, original_height = image.get_size()
        scale_factor = target_width / original_width
        new_height = int(original_height * scale_factor)
        return pygame.transform.smoothscale(image, (target_width, new_height))