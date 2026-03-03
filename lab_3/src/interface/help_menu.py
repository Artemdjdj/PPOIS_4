import sys

import pygame
from pygame import Surface

from src.interface.button import Button
from src.settings.settings import SCREEN_WIDTH, BUTTON_WIDTH, COORD_Y_FIRST_BUTTON, BASIC_BACKGROUND_HOVER_COLOR, \
    BASIC_BACKGROUND_COLOR, BASIC_FONT, BASIC_FONT_SIZE, COORD_Y_BACK_BUTTON, BUTTON_HEIGHT, BASIC_COLOR, NAME_BACK, \
    HELP_MENU_BACKGROUND_IMAGE, SCREEN_HEIGHT, FILE_RULES_PATH, RULES_COLOR, COORD_Y_START_TEXT, RULES_FONT_SIZE
from src.settings.state import State
from src.utils.reader import TxtReader


class HelpMenu:
    def __init__(self, screen:Surface, )->None:
        self._screen = screen
        self._back_button = Button(SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2, COORD_Y_BACK_BUTTON, BUTTON_WIDTH, BUTTON_HEIGHT, BASIC_COLOR,
                   BASIC_BACKGROUND_COLOR, BASIC_BACKGROUND_HOVER_COLOR, NAME_BACK,
                   pygame.font.Font(BASIC_FONT, BASIC_FONT_SIZE), State.MENU)
        reader = TxtReader(FILE_RULES_PATH)
        self._rules = reader.read()
        self._background = pygame.image.load(HELP_MENU_BACKGROUND_IMAGE).convert_alpha()
        self._background = pygame.transform.scale(self._background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw(self)->None:
        self._screen.blit(self._background, (0, 0))
        rule_lines = self._rules.split('\n')
        y_pos = COORD_Y_START_TEXT
        for line in rule_lines:
            text_surface = pygame.font.Font(BASIC_FONT, RULES_FONT_SIZE).render(line, True, RULES_COLOR)
            self._screen.blit(text_surface, (SCREEN_WIDTH//3, y_pos))
            y_pos += text_surface.get_height()
        self._back_button.draw(self._screen)

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            result = self._back_button.check_event(event)
            if result is not None:
                return result
        return None


