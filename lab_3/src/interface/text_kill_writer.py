from typing import Tuple

import pygame

from src.settings.settings import ALPHA


class TextKillWriter:
    def __init__(self, x: int, y: int, text: str, font: str, font_size: int, color: Tuple[int, int, int], fps: int = 60,
                 speed_y=1.6) -> None:
        self.x = x
        self.y = y
        self.text = text
        self.font = pygame.font.Font(font, font_size)
        self.font_size = font_size
        self.color = color
        self.fps = fps
        self.max_fps = fps
        self.speed_y = speed_y
        self.alive = True
        self.alpha = ALPHA

    def update(self):
        self.y += self.speed_y
        self.fps -= 1
        self.alpha = int(ALPHA * (self.fps / self.max_fps))
        if self.fps <= 0:
            self.alive = False

    def draw(self, screen):
        text_surface = self.font.render(self.text, True, self.color)
        text_surface.set_alpha(self.alpha)
        rect = text_surface.get_rect(center=(int(self.x), int(self.y)))
        screen.blit(text_surface, rect)
