import sys

import pygame

from src.interface.menu import Menu
from src.settings.settings import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_NAME, BACKGROUND_COLOR
from src.settings.state import State


class Moorhuhn:
    """Класс для управлением ресурсами и поведением игры"""

    def __init__(self)->None:
        pygame.init()
        self._screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_NAME)
        self._state = State.MENU
        self._menu = Menu(self._screen)

    def _draw_background(self):
        self._screen.fill(BACKGROUND_COLOR)

    def run_game(self)->None:
        while True:
            pygame.display.flip()
            if self._state == State.MENU:
                self._menu.draw()
                new_state = self._menu.check_event()
                if new_state is not None:
                    self._state = new_state
            elif self._state == State.QUIT:
                sys.exit()
