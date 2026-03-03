import sys
from typing import Optional

import pygame

from src.interface.button import Button
from src.settings.state import State
from src.settings.settings import SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, BASIC_FONT, BASIC_FONT_SIZE, \
    BASIC_BACKGROUND_COLOR, BASIC_BACKGROUND_HOVER_COLOR, NAME_PLAY, NAME_TABLE_RECORD, NAME_HELP, NAME_QUIT, \
    COORD_Y_FIRST_BUTTON, HEIGHT_BETWEEN_BUTTONS, MENU_BACKGROUND_IMAGE, BASIC_COLOR


class Menu:
    def __init__(self, screen: pygame.Surface) -> None:
        self._screen = screen
        self._buttons = [
            Button(SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2, COORD_Y_FIRST_BUTTON, BUTTON_WIDTH, BUTTON_HEIGHT, BASIC_COLOR,
                   BASIC_BACKGROUND_COLOR, BASIC_BACKGROUND_HOVER_COLOR, NAME_PLAY,
                   pygame.font.Font(BASIC_FONT, BASIC_FONT_SIZE), State.PLAY),
            Button(SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2, COORD_Y_FIRST_BUTTON+HEIGHT_BETWEEN_BUTTONS, BUTTON_WIDTH, BUTTON_HEIGHT, BASIC_COLOR,
                   BASIC_BACKGROUND_COLOR, BASIC_BACKGROUND_HOVER_COLOR, NAME_TABLE_RECORD,
                   pygame.font.Font(BASIC_FONT, BASIC_FONT_SIZE), State.RECORD_TABLE),
            Button(SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2, COORD_Y_FIRST_BUTTON+2*HEIGHT_BETWEEN_BUTTONS, BUTTON_WIDTH, BUTTON_HEIGHT, BASIC_COLOR,
                   BASIC_BACKGROUND_COLOR, BASIC_BACKGROUND_HOVER_COLOR, NAME_HELP,
                   pygame.font.Font(BASIC_FONT, BASIC_FONT_SIZE), State.HELP),
            Button(SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2, COORD_Y_FIRST_BUTTON+3*HEIGHT_BETWEEN_BUTTONS, BUTTON_WIDTH, BUTTON_HEIGHT, BASIC_COLOR,
                   BASIC_BACKGROUND_COLOR, BASIC_BACKGROUND_HOVER_COLOR, NAME_QUIT,
                   pygame.font.Font(BASIC_FONT, BASIC_FONT_SIZE), State.QUIT),
        ]
        self._background = pygame.image.load(MENU_BACKGROUND_IMAGE).convert_alpha()
        self._background = pygame.transform.scale(self._background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw(self) -> None:
        self._screen.blit(self._background, (0, 0))
        for button in self._buttons:
            button.draw(self._screen)

    def check_event(self) -> Optional[State]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            for button in self._buttons:
                result = button.check_event(event)
                if result is not None:
                    return result
        return None
