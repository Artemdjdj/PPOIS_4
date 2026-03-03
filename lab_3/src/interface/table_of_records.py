import sys

import pygame
from pygame import Surface

from src.interface.button import Button
from src.interface.mixins.additional_menu import AdditionalMenuMixin
from src.settings.settings import SCREEN_WIDTH, BUTTON_WIDTH, COORD_Y_BACK_BUTTON, BUTTON_HEIGHT, BASIC_COLOR, \
    BASIC_BACKGROUND_COLOR, BASIC_BACKGROUND_HOVER_COLOR, NAME_BACK, BASIC_FONT, BASIC_FONT_SIZE, \
    TABLE_RECORDS_BACKGROUND_IMAGE, SCREEN_HEIGHT
from src.settings.state import State


class TableRecords(AdditionalMenuMixin):
    def __init__(self, screen: Surface) -> None:
        super().__init__(screen, TABLE_RECORDS_BACKGROUND_IMAGE)

    def _write_leaders(self) -> None:
        pass
