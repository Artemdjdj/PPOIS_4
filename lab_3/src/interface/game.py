import sys
from typing import Optional

import pygame
from pygame import Surface
from pygame.time import Clock

from src.factories.bird_factory import SittingChickenFactory, FlyingChickenFactory
from src.interface.button import Button
from src.interface.cursor import Cursor
from src.interface.layer import SkyLayer, FieldLayer, GameLayer
from src.settings.state import State
from src.settings.settings import SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, BASIC_FONT, BASIC_FONT_SIZE, \
    BASIC_BACKGROUND_COLOR, BASIC_BACKGROUND_HOVER_COLOR, NAME_PLAY, NAME_TABLE_RECORD, NAME_HELP, NAME_QUIT, \
    COORD_Y_FIRST_BUTTON, HEIGHT_BETWEEN_BUTTONS, MENU_BACKGROUND_IMAGE, BASIC_COLOR, GAME_BACKGROUND_IMAGE, BASE_DIR, \
    SPEED_FIRST_LAYER, SPEED_SECOND_LAYER, SPEED_THIRD_LAYER, DEFAULT_SPEED, SHOOT_EFFECT, CROSSHAIR_IMAGE, FIRST_LAYER, \
    THIRD_LAYER, SECOND_LAYER, HEIGHT_FLYING_CHICKEN, FIRST_LAYER_HEIGHT, \
    SECOND_LAYER_HEIGHT, THIRD_LAYER_HEIGHT, INDENT_BEFORE_MAX_HEIGHT, INDENT_BETWEEN_LAYERS, DEFAULT_SPEED_WORLD, FPS, \
    CAR_COORD_X, CAR_COORD_Y, OVEN_COORD_X, OVEN_COORD_Y
from src.sprites.car import Car
from src.sprites.chicken import SittingChicken, FlyingChicken
from src.sprites.oven import Oven


class Game:
    def __init__(self, screen: pygame.Surface, clock:Clock) -> None:
        self._screen = screen

        self._layer_sky = SkyLayer(pygame.image.load(FIRST_LAYER).convert_alpha(), 'far',SPEED_FIRST_LAYER, (INDENT_BETWEEN_LAYERS,
                            FIRST_LAYER_HEIGHT), DEFAULT_SPEED_WORLD)
        self._layer_field = FieldLayer(pygame.image.load(SECOND_LAYER).convert_alpha(), 'mid', SPEED_SECOND_LAYER,
                                   (FIRST_LAYER_HEIGHT+INDENT_BETWEEN_LAYERS, FIRST_LAYER_HEIGHT + SECOND_LAYER_HEIGHT-INDENT_BETWEEN_LAYERS))
        self._layer_game = GameLayer(pygame.image.load(THIRD_LAYER).convert_alpha(), 'game', SPEED_THIRD_LAYER,
                                      (FIRST_LAYER_HEIGHT + SECOND_LAYER_HEIGHT,
                                       FIRST_LAYER_HEIGHT + SECOND_LAYER_HEIGHT + THIRD_LAYER_HEIGHT + INDENT_BETWEEN_LAYERS - INDENT_BEFORE_MAX_HEIGHT - INDENT_BETWEEN_LAYERS))

        self._layers = [self._layer_sky, self._layer_field, self._layer_game]

        self._layer_game.car = Car(CAR_COORD_X, CAR_COORD_Y, SPEED_THIRD_LAYER)
        self._layer_game.oven = Oven(OVEN_COORD_X, OVEN_COORD_Y, SPEED_THIRD_LAYER)
        self._cursor = Cursor()
        self._dt = clock.tick(FPS) / 1000.0

        self._scroll_position = SCREEN_WIDTH // 2
        self._shoot_effect = pygame.mixer.Sound(SHOOT_EFFECT)
        self._shoot_effect.set_volume(0.6)

    def create_sitting_chickens_game(self, count: int):
        self._layer_game.create_chickens(count)

    def create_sitting_chickens_field(self, count: int):
        self._layer_field.create_chickens(count)

    def create_flying_chickens(self, count: int):
        self._layer_sky.create_chickens(count)

    def draw(self) -> None:
        for x in range(3):
            self._layer_sky.draw(self._screen, x, self._scroll_position)
            self._layer_field.draw(self._screen, x, self._scroll_position)
            self._layer_game.draw(self._screen, x, self._scroll_position)

        for chicken in self._layer_sky.chickens:
            chicken.update(self._dt)

        self._layer_game.car.draw(self._screen, self._scroll_position)
        self._layer_game.oven.draw(self._screen, self._scroll_position)
        for layer in self._layers:
            for chicken in layer.chickens:
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
