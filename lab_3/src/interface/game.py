import sys
from typing import Optional

import pygame

from src.interface.button import Button
from src.settings.state import State
from src.settings.settings import SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, BASIC_FONT, BASIC_FONT_SIZE, \
    BASIC_BACKGROUND_COLOR, BASIC_BACKGROUND_HOVER_COLOR, NAME_PLAY, NAME_TABLE_RECORD, NAME_HELP, NAME_QUIT, \
    COORD_Y_FIRST_BUTTON, HEIGHT_BETWEEN_BUTTONS, MENU_BACKGROUND_IMAGE, BASIC_COLOR, GAME_BACKGROUND_IMAGE, BASE_DIR, \
    SPEED_FIRST_LAYER, SPEED_SECOND_LAYER, SPEED_THIRD_LAYER, DEFAULT_SPEED


class Game:
    def __init__(self, screen: pygame.Surface) -> None:
        self._screen = screen
        self._layers = []
        self._layer_1 = pygame.image.load(BASE_DIR / f"assets/images/new_layer_{1}.png").convert_alpha()
        self._layer_2 = pygame.image.load(BASE_DIR / f"assets/images/new_layer_{2}.png").convert_alpha()
        self._layer_3 = pygame.image.load(BASE_DIR / f"assets/images/new_layer_{3}.png").convert_alpha()
        self._layer_width = self._layer_1.get_width()
        self._scroll_position = 0

    def draw(self)->None:
        for x in range(3):
            self._screen.blit(self._layer_1, ((x*self._layer_width) - self._scroll_position*SPEED_FIRST_LAYER,0))
            self._screen.blit(self._layer_2, ((x * self._layer_width) - self._scroll_position * SPEED_SECOND_LAYER, 0))
            self._screen.blit(self._layer_3, ((x * self._layer_width) - self._scroll_position * SPEED_THIRD_LAYER, 0))

    def check_event(self) -> Optional[State]:
        key = pygame.key.get_pressed()
        if (key[pygame.K_LEFT] or key[pygame.K_a]) and self._scroll_position > 0:
            self._scroll_position -= DEFAULT_SPEED
        if (key[pygame.K_RIGHT] or key[pygame.K_d]) and self._scroll_position < SCREEN_WIDTH:
            self._scroll_position += DEFAULT_SPEED
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        return None
