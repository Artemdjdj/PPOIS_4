import sys
from typing import Optional

import pygame
from pygame import Surface
from pygame.time import Clock

from src.factories.bird_factory import SittingChickenFactory, FlyingChickenFactory
from src.interface.button import Button
from src.interface.cursor import Cursor
from src.settings.state import State
from src.settings.settings import SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, BASIC_FONT, BASIC_FONT_SIZE, \
    BASIC_BACKGROUND_COLOR, BASIC_BACKGROUND_HOVER_COLOR, NAME_PLAY, NAME_TABLE_RECORD, NAME_HELP, NAME_QUIT, \
    COORD_Y_FIRST_BUTTON, HEIGHT_BETWEEN_BUTTONS, MENU_BACKGROUND_IMAGE, BASIC_COLOR, GAME_BACKGROUND_IMAGE, BASE_DIR, \
    SPEED_FIRST_LAYER, SPEED_SECOND_LAYER, SPEED_THIRD_LAYER, DEFAULT_SPEED, SHOOT_EFFECT, CROSSHAIR_IMAGE, FIRST_LAYER, \
    THIRD_LAYER, SECOND_LAYER, HEIGHT_FLYING_CHICKEN, FIRST_LAYER_HEIGHT, \
    SECOND_LAYER_HEIGHT, THIRD_LAYER_HEIGHT, INDENT_BEFORE_MAX_HEIGHT, INDENT_BETWEEN_LAYERS, DEFAULT_SPEED_WORLD
from src.sprites.chicken import SittingChicken, FlyingChicken


class Game:
    def __init__(self, screen: pygame.Surface, clock:Clock) -> None:
        self._screen = screen
        self._layer_1 = pygame.image.load(FIRST_LAYER).convert_alpha()
        self._layer_2 = pygame.image.load(SECOND_LAYER).convert_alpha()
        self._layer_3 = pygame.image.load(THIRD_LAYER).convert_alpha()
        self._layer_width = self._layer_1.get_width()
        self._cursor = Cursor()
        self._dt = clock.tick(60) / 1000.0

        self._layers_config = [
            {
                'name': 'far',
                'group': pygame.sprite.Group(),
                'speed': SPEED_FIRST_LAYER,
                'y_range': (INDENT_BETWEEN_LAYERS,
                            FIRST_LAYER_HEIGHT),
                'factory': None
            },
            {
                'name': 'mid',
                'group': pygame.sprite.Group(),
                'speed': SPEED_SECOND_LAYER,
                'y_range': (FIRST_LAYER_HEIGHT+INDENT_BETWEEN_LAYERS, FIRST_LAYER_HEIGHT + SECOND_LAYER_HEIGHT-INDENT_BETWEEN_LAYERS),
                'factory': None
            },
            {
                'name': 'near',
                'group': pygame.sprite.Group(),
                'speed': SPEED_THIRD_LAYER,
                'y_range': (FIRST_LAYER_HEIGHT + SECOND_LAYER_HEIGHT,
                            FIRST_LAYER_HEIGHT + SECOND_LAYER_HEIGHT + THIRD_LAYER_HEIGHT+INDENT_BETWEEN_LAYERS - INDENT_BEFORE_MAX_HEIGHT-INDENT_BETWEEN_LAYERS),
                'factory': None
            }
        ]

        for i in range(1, len(self._layers_config)):
            layer = self._layers_config[i]
            layer['factory'] = SittingChickenFactory(layer['group'])


        self._layers_config[0]['factory'] = FlyingChickenFactory(self._layers_config[0]['group'])
        self._scroll_position = SCREEN_WIDTH // 2
        self._shoot_effect = pygame.mixer.Sound(SHOOT_EFFECT)
        self._shoot_effect.set_volume(0.6)

    def create_sitting_chickens(self, counts: list[int]):
        for layer, count in zip(self._layers_config, counts):
            min_y, max_y = layer['y_range']
            for _ in range(count):
                chicken = layer['factory'].create(min_y, max_y, layer['speed'])
                if chicken:
                    layer['group'].add(chicken)

    def create_flying_chickens(self, counts: int):
        for _ in range(counts):
            layer = self._layers_config[0]
            chicken = layer['factory'].create(0, FIRST_LAYER_HEIGHT, DEFAULT_SPEED_WORLD)
            if chicken:
                layer['group'].add(chicken)

    def draw(self) -> None:
        for x in range(3):
            self._screen.blit(self._layer_1, ((x * self._layer_width) - self._scroll_position * SPEED_FIRST_LAYER, 0))
            self._screen.blit(self._layer_2, ((x * self._layer_width) - self._scroll_position * SPEED_SECOND_LAYER, 0))
            self._screen.blit(self._layer_3, ((x * self._layer_width) - self._scroll_position * SPEED_THIRD_LAYER, 0))

        for chicken in self._layers_config[0]['group']:
            chicken.update(self._dt)

        for layer in self._layers_config:
            for chicken in layer['group']:
                chicken.draw(self._screen, self._scroll_position)

        self._cursor.draw(self._screen)

    def check_event(self) -> Optional[State]:
        key = pygame.key.get_pressed()
        if (key[pygame.K_LEFT] or key[pygame.K_a]) and self._scroll_position > 0:
            self._scroll_position -= DEFAULT_SPEED
        if (key[pygame.K_RIGHT] or key[pygame.K_d]) and self._scroll_position < SCREEN_WIDTH:
            self._scroll_position += DEFAULT_SPEED
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._shoot_effect.play()
        return None
