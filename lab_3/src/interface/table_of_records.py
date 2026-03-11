import sys

import pygame
from pygame import Surface

from src.interface.button import Button
from src.interface.mixins.additional_menu import AdditionalMenuMixin
from src.interface.writer import Writer
from src.settings.settings import SCREEN_WIDTH, BUTTON_WIDTH, COORD_Y_BACK_BUTTON, BUTTON_HEIGHT, BASIC_COLOR, \
    BASIC_BACKGROUND_COLOR, BASIC_BACKGROUND_HOVER_COLOR, NAME_BACK, BASIC_FONT, BASIC_FONT_SIZE, \
    TABLE_RECORDS_BACKGROUND_IMAGE, SCREEN_HEIGHT, COORD_Y_START_TABLE_RECORDS, RULES_FONT_SIZE, \
    RULES_COLOR, COORD_X_RECORD, COORD_X_NAME, COORD_X_NUMBER, NAME_COLUMN_NUMBER, NAME_COLUMN_NAME, NAME_COLUMN_RECORD, \
    COLUMN_NAME_FONT_SIZE, COORD_Y_START_TABLE_RECORDS_COLUMN, FILE_TABLE_LEADERS
from src.settings.state import State
from src.utils.loader import JsonLeadersLoader


class TableRecords(AdditionalMenuMixin):
    def __init__(self, screen: Surface, leaders) -> None:
        self._leaders = leaders
        super().__init__(screen, NAME_BACK, TABLE_RECORDS_BACKGROUND_IMAGE)

    def _write_leaders(self) -> None:
        y_pos = COORD_Y_START_TABLE_RECORDS

        Writer(NAME_COLUMN_NUMBER, BASIC_FONT, COLUMN_NAME_FONT_SIZE, RULES_COLOR,
               (COORD_X_NUMBER, COORD_Y_START_TABLE_RECORDS_COLUMN)).draw(self._screen)
        Writer(NAME_COLUMN_NAME, BASIC_FONT, COLUMN_NAME_FONT_SIZE, RULES_COLOR,
               (COORD_X_NAME, COORD_Y_START_TABLE_RECORDS_COLUMN)).draw(self._screen)
        Writer(NAME_COLUMN_RECORD, BASIC_FONT, COLUMN_NAME_FONT_SIZE, RULES_COLOR,
               (COORD_X_RECORD, COORD_Y_START_TABLE_RECORDS_COLUMN)).draw(self._screen)

        for i,leader in enumerate(self._leaders):
            number_writer = Writer(str(i+1), BASIC_FONT, RULES_FONT_SIZE, RULES_COLOR,
                                   (COORD_X_NUMBER, y_pos))
            Writer(str(leader[0]), BASIC_FONT, RULES_FONT_SIZE, RULES_COLOR, (COORD_X_NAME, y_pos)).draw(
                self._screen)
            Writer(str(leader[1]), BASIC_FONT, RULES_FONT_SIZE, RULES_COLOR, (COORD_X_RECORD, y_pos)).draw(
                self._screen)
            number_writer.draw(self._screen)
            y_pos += number_writer.rect.height

    def draw(self)->None:
        super().draw()
        self._write_leaders()
