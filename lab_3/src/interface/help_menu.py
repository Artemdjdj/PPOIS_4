import sys

import pygame
from pygame import Surface

from src.interface.button import Button
from src.interface.mixins.additional_menu import AdditionalMenuMixin
from src.settings.settings import SCREEN_WIDTH, BUTTON_WIDTH, COORD_Y_FIRST_BUTTON, BASIC_BACKGROUND_HOVER_COLOR, \
    BASIC_BACKGROUND_COLOR, BASIC_FONT, BASIC_FONT_SIZE, COORD_Y_BACK_BUTTON, BUTTON_HEIGHT, BASIC_COLOR, NAME_BACK, \
    HELP_MENU_BACKGROUND_IMAGE, SCREEN_HEIGHT, FILE_RULES_PATH, RULES_COLOR, COORD_Y_START_TEXT, RULES_FONT_SIZE
from src.settings.state import State
from src.utils.reader import TxtReader


class HelpMenu(AdditionalMenuMixin):
    def __init__(self, screen: Surface) -> None:
        super().__init__(screen, HELP_MENU_BACKGROUND_IMAGE)
        reader = TxtReader(FILE_RULES_PATH)
        self._rules = reader.read()

    def draw(self) -> None:
        super().draw()
        rule_lines = self._rules.split('\n')
        y_pos = COORD_Y_START_TEXT
        for line in rule_lines:
            text_surface = pygame.font.Font(BASIC_FONT, RULES_FONT_SIZE).render(line, True, RULES_COLOR)
            self._screen.blit(text_surface, (SCREEN_WIDTH // 3, y_pos))
            y_pos += text_surface.get_height()
