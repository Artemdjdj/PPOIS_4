import sys

import pygame
from pygame import Surface

from src.interface.button import Button
from src.interface.mixins.additional_menu import AdditionalMenuMixin
from src.settings.settings import SCREEN_WIDTH, BUTTON_WIDTH, COORD_Y_BACK_BUTTON, BUTTON_HEIGHT, BASIC_COLOR, \
    BASIC_BACKGROUND_COLOR, BASIC_BACKGROUND_HOVER_COLOR, NAME_BACK, BASIC_FONT, BASIC_FONT_SIZE, \
    TABLE_RECORDS_BACKGROUND_IMAGE, SCREEN_HEIGHT, TEST_LEADERS, COORD_Y_START_TABLE_RECORDS, RULES_FONT_SIZE, \
    RULES_COLOR, COORD_X_RECORD, COORD_X_NAME, COORD_X_NUMBER
from src.settings.state import State


class TableRecords(AdditionalMenuMixin):
    def __init__(self, screen: Surface) -> None:
        super().__init__(screen, TABLE_RECORDS_BACKGROUND_IMAGE)

    def _write_leaders(self) -> None:
        leaders = TEST_LEADERS.copy()
        y_pos = COORD_Y_START_TABLE_RECORDS
        for leader in leaders:
            text_number = pygame.font.Font(BASIC_FONT, RULES_FONT_SIZE).render(str(leader["number"]), True, RULES_COLOR)
            text_name = pygame.font.Font(BASIC_FONT, RULES_FONT_SIZE).render(str(leader["name"]), True, RULES_COLOR)
            text_record = pygame.font.Font(BASIC_FONT, RULES_FONT_SIZE).render(str(leader["record"]), True, RULES_COLOR)
            self._screen.blit(text_number, (COORD_X_NUMBER, y_pos))
            self._screen.blit(text_name, (COORD_X_NAME, y_pos))
            self._screen.blit(text_record, (COORD_X_RECORD, y_pos))
            y_pos += text_number.get_height()

    def draw(self)->None:
        super().draw()
        self._write_leaders()
