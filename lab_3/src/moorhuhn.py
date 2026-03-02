import sys

import pygame

from settings import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_NAME, BACKGROUND_COLOR


class Moorhuhn:
    """Класс для управлением ресурсами и поведением игры"""

    def __init__(self)->None:
        pygame.init()
        self._screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_NAME)

    def _draw_background(self):
        self._screen.fill(BACKGROUND_COLOR)

    def run_game(self)->None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self._draw_background()
            pygame.display.flip()
