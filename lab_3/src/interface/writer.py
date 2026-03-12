from typing import Tuple

import pygame


class Writer:
    def __init__(self, text, font_name, font_size, color: Tuple[int, int, int], pos: Tuple[int, int],
                 antialias: bool = True) -> None:
        self.text = text
        self.color = color
        self.pos = pos
        self.antialias = antialias
        self.font = pygame.font.Font(font_name, font_size)
        self._render()

    def _render(self):
        self.surface = self.font.render(self.text, self.antialias, self.color)
        self.rect = self.surface.get_rect(topleft=self.pos)

    def set_text(self, text: str):
        self.text = text
        self._render()

    def set_pos(self, pos: Tuple[int, int]):
        self.pos = pos
        self.rect.topleft = pos

    def draw(self, screen: pygame.Surface):
        screen.blit(self.surface, self.rect)
