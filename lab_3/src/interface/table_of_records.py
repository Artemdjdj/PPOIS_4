import sys

import pygame
from pygame import Surface

from src.interface.button import Button
from src.settings.settings import SCREEN_WIDTH, BUTTON_WIDTH, COORD_Y_BACK_BUTTON, BUTTON_HEIGHT, BASIC_COLOR, \
    BASIC_BACKGROUND_COLOR, BASIC_BACKGROUND_HOVER_COLOR, NAME_BACK, BASIC_FONT, BASIC_FONT_SIZE, \
    TABLE_RECORDS_BACKGROUND_IMAGE, SCREEN_HEIGHT
from src.settings.state import State


class TableRecords:
    def __init__(self, screen:Surface):
        self._screen = screen
        self._back_button = Button(SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2, COORD_Y_BACK_BUTTON, BUTTON_WIDTH,
                                   BUTTON_HEIGHT, BASIC_COLOR,
                                   BASIC_BACKGROUND_COLOR, BASIC_BACKGROUND_HOVER_COLOR, NAME_BACK,
                                   pygame.font.Font(BASIC_FONT, BASIC_FONT_SIZE), State.MENU)

        self._background = pygame.image.load(TABLE_RECORDS_BACKGROUND_IMAGE).convert_alpha()
        self._background = pygame.transform.scale(self._background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw(self):
        self._screen.blit(self._background, (0, 0))
        self._back_button.draw(self._screen)

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            result = self._back_button.check_event(event)
            if result is not None:
                return result
        return None