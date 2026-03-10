import random
import sys
import time
from typing import Optional, Text, Tuple

import pygame
from pygame import Surface
from pygame.time import Clock

from src.factories.bird_factory import SittingChickenFactory, FlyingChickenFactory
from src.factories.cartridge_factory import CartridgesFactory
from src.interface.button import Button
from src.interface.cursor import Cursor
from src.interface.layer import SkyLayer, FieldLayer, GameLayer
from src.interface.sound_player import SoundPlayer
from src.interface.text_kill_writer import TextKillWriter
from src.interface.writer import Writer
from src.objects.balloon import Balloon
from src.objects.hedgehog import Hedgehog
from src.objects.puddle import Puddle
from src.objects.toilet import Toilet
from src.settings.state import State
from src.settings.settings import SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, BASIC_FONT, BASIC_FONT_SIZE, \
    BASIC_BACKGROUND_COLOR, BASIC_BACKGROUND_HOVER_COLOR, NAME_PLAY, NAME_TABLE_RECORD, NAME_HELP, NAME_QUIT, \
    COORD_Y_FIRST_BUTTON, HEIGHT_BETWEEN_BUTTONS, MENU_BACKGROUND_IMAGE, BASIC_COLOR, GAME_BACKGROUND_IMAGE, BASE_DIR, \
    SPEED_FIRST_LAYER, SPEED_SECOND_LAYER, SPEED_THIRD_LAYER, DEFAULT_SPEED, SHOOT_EFFECT, CROSSHAIR_IMAGE, FIRST_LAYER, \
    THIRD_LAYER, SECOND_LAYER, HEIGHT_FLYING_CHICKEN, FIRST_LAYER_HEIGHT, \
    SECOND_LAYER_HEIGHT, THIRD_LAYER_HEIGHT, INDENT_BEFORE_MAX_HEIGHT, INDENT_BETWEEN_LAYERS, DEFAULT_SPEED_WORLD, FPS, \
    CAR_COORD_X, CAR_COORD_Y, OVEN_COORD_X, OVEN_COORD_Y, HEDGEHOG_COORD_X, HEDGEHOG_COORD_Y, BALLOON_COORD_Y, \
    BALLOON_COORD_X, TOILET_COORD_Y, TOILET_COORD_X, CARTRIDGE_START_Y, CARTRIDGE_START_X, SPACE_BETWEEN_CARTRIDGES, \
    EMPTY_CLIP_EFFECT, RELOAD_CLIP_EFFECT, RELOAD_TEXT_SIZE, RELOAD_TEXT_COLOR, RELOAD_CLIP_TEXT, SCORE_TEXT_SIZE, SPACE_SCORE_X, SPACE_INFO_Y, SPACE_TIME_X, PUDDLE_COORD_X, PUDDLE_COORD_Y, \
    MAX_COUNT_CHICKENS_IN_LAYER
from src.objects.car import Car
from src.objects.chicken import SittingChicken, FlyingChicken
from src.objects.oven import Oven


class Game:
    def __init__(self, screen: pygame.Surface, dt) -> None:
        self._screen = screen

        self._layer_sky = SkyLayer(pygame.image.load(FIRST_LAYER).convert_alpha(), 'far', SPEED_FIRST_LAYER,
                                   (INDENT_BETWEEN_LAYERS,
                                    FIRST_LAYER_HEIGHT), DEFAULT_SPEED_WORLD)
        self._layer_field = FieldLayer(pygame.image.load(SECOND_LAYER).convert_alpha(), 'mid', SPEED_SECOND_LAYER,
                                       (FIRST_LAYER_HEIGHT + INDENT_BETWEEN_LAYERS,
                                        FIRST_LAYER_HEIGHT + SECOND_LAYER_HEIGHT - INDENT_BETWEEN_LAYERS))
        self._layer_game = GameLayer(pygame.image.load(THIRD_LAYER).convert_alpha(), 'game', SPEED_THIRD_LAYER,
                                     (FIRST_LAYER_HEIGHT + SECOND_LAYER_HEIGHT,
                                      FIRST_LAYER_HEIGHT + SECOND_LAYER_HEIGHT + THIRD_LAYER_HEIGHT + INDENT_BETWEEN_LAYERS - INDENT_BEFORE_MAX_HEIGHT - INDENT_BETWEEN_LAYERS))

        self._layers = [self._layer_sky, self._layer_field, self._layer_game]

        self._create_objects()
        self._cursor = Cursor()

        self._clip = CartridgesFactory(5, CARTRIDGE_START_X, CARTRIDGE_START_Y, SPACE_BETWEEN_CARTRIDGES)
        self._dt = dt

        self._scroll_position = SCREEN_WIDTH // 2
        self._sound_player = SoundPlayer()


        self._reload_clip_text = Writer(RELOAD_CLIP_TEXT, BASIC_FONT, RELOAD_TEXT_SIZE, RELOAD_TEXT_COLOR,
                                        (CARTRIDGE_START_X - SPACE_BETWEEN_CARTRIDGES * 5, CARTRIDGE_START_Y))
        self._score_text = Writer("", BASIC_FONT, SCORE_TEXT_SIZE, RELOAD_TEXT_COLOR,
                                  (SPACE_SCORE_X, SPACE_INFO_Y))
        self._time_text = Writer("", BASIC_FONT, SCORE_TEXT_SIZE, RELOAD_TEXT_COLOR,
                                 (SPACE_TIME_X, SPACE_INFO_Y))

        self._max_count_chickens_in_layer = MAX_COUNT_CHICKENS_IN_LAYER


        self._kill_scores = []

        self._total_kill_points = 0

    def spawn_chickens(self):
        actions = [
            (self.create_sitting_chickens_game,
             lambda: (random.randint(0, max(0, MAX_COUNT_CHICKENS_IN_LAYER - len(self._layer_game.chickens))),)),
            (self.create_moving_chickens_field, lambda: (
                (random.randint(0, max(0, (MAX_COUNT_CHICKENS_IN_LAYER - len(self._layer_field.chickens)) // 3)),
                 random.randint(0, max(0, (MAX_COUNT_CHICKENS_IN_LAYER - len(self._layer_field.chickens))))),
            )),
            (self.create_flying_chickens,
             lambda: (random.randint(0, max(0, MAX_COUNT_CHICKENS_IN_LAYER - len(self._layer_sky.chickens))),))
        ]
        func, args_gen = random.choice(actions)
        func(*args_gen())

    @property
    def total_kill_points(self) -> int:
        return self._total_kill_points

    def create_sitting_chickens_game(self, count: int):
        self._layer_game.create_chickens(count)

    def create_moving_chickens_field(self, counts: Tuple[int, int]):
        self._layer_field.create_chickens(counts)

    def create_flying_chickens(self, count: int):
        self._layer_sky.create_chickens(count)

    def update_time(self, time:str)->None:
        self._time_text.set_text(time)

    def update_dt(self, dt: float) -> None:
        self._dt = dt

    def _update_score(self, score: int) -> None:
        self._score_text.set_text(str(score))

    def _create_objects(self)->None:
        self._layer_game.add_object(Car(CAR_COORD_X, CAR_COORD_Y, SPEED_THIRD_LAYER))
        self._layer_game.add_object(Puddle(PUDDLE_COORD_X, PUDDLE_COORD_Y, SPEED_THIRD_LAYER))
        self._layer_game.add_object(Hedgehog(HEDGEHOG_COORD_X, HEDGEHOG_COORD_Y, SPEED_THIRD_LAYER))
        self._layer_game.add_object(Oven(OVEN_COORD_X, OVEN_COORD_Y, SPEED_THIRD_LAYER))

        self._layer_sky.add_object(Balloon(BALLOON_COORD_X, BALLOON_COORD_Y, SPEED_THIRD_LAYER))
        self._layer_field.add_object(Toilet(TOILET_COORD_X, TOILET_COORD_Y, SPEED_SECOND_LAYER))

    def reset(self):
        self._layer_game.clear()
        self._layer_field.clear()
        self._layer_sky.clear()
        self._create_objects()
        self._total_kill_points = 0
        # self.create_moving_chickens_field((4, 6))
        # self.create_sitting_chickens_game(10)
        # self.create_flying_chickens(10)
        self._kill_scores.clear()
        self._clip.create()

    def draw(self) -> None:
        for x in range(3):
            self._layer_sky.draw(self._screen, x, self._scroll_position)
            self._layer_field.draw(self._screen, x, self._scroll_position)
            self._layer_game.draw(self._screen, x, self._scroll_position)

        for layer in self._layers:
            for element in layer.objects:
                element.animate()
                element.draw(self._screen, self._scroll_position)

            for chicken in layer.chickens:
                chicken.update(self._dt)
                chicken.animate()
                chicken.draw(self._screen, self._scroll_position)

        self._update_score(self._total_kill_points)
        self._score_text.draw(self._screen)
        self._time_text.draw(self._screen)

        for text in self._kill_scores:
            text.update()
            text.draw(self._screen)

        self._kill_scores = [t for t in self._kill_scores if t.alive]

        if self._clip.cartridges:
            for cartridge in self._clip.cartridges:
                cartridge.draw(self._screen, self._scroll_position)
        else:
            self._reload_clip_text.draw(self._screen)

        self._cursor.draw(self._screen)

    def _update_kill_points(self, point:int)->None:
        if point + self._total_kill_points <0:
            self._total_kill_points = 0
        else:
            self._total_kill_points += point

    def check_event(self) -> Optional[State]:
        key = pygame.key.get_pressed()
        if (key[pygame.K_LEFT] or key[pygame.K_a]) and self._scroll_position > 0:
            self._scroll_position -= DEFAULT_SPEED
        if (key[pygame.K_RIGHT] or key[pygame.K_d]) and self._scroll_position < SCREEN_WIDTH:
            self._scroll_position += DEFAULT_SPEED
        if key[pygame.K_r]:
            if len(self._clip.cartridges) == 0:
                self._clip.create()
                self._sound_player.set_sound(RELOAD_CLIP_EFFECT)
                self._sound_player.play(0.6)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if len(self._clip.cartridges) != 0:
                    self._clip.delete()
                    self._sound_player.set_sound(SHOOT_EFFECT)
                    self._sound_player.play(0.6)
                    aim_x, aim_y = self._cursor.get_center()
                    for layer in self._layers:
                        for chicken in layer.chickens:
                            screen_chicken_x = chicken.rect.x - self._scroll_position * chicken.layer_speed
                            screen_chicken_y = chicken.rect.y
                            aim_mask = pygame.mask.Mask((1, 1), fill=True)
                            offset = (int(aim_x-screen_chicken_x), int(aim_y-screen_chicken_y))
                            if chicken.mask.overlap(aim_mask, offset):
                                chicken.play(0.6)
                                chicken.shoot()
                                text = chicken.score
                                if text:
                                    self._kill_scores.append(TextKillWriter(
                                        chicken.rect.x - self._scroll_position * chicken.layer_speed,
                                        chicken.rect.top+10,
                                        str(chicken.score),
                                        BASIC_FONT,
                                        SCORE_TEXT_SIZE,
                                        BASIC_COLOR
                                    ))
                                    self._update_kill_points(chicken.score)
                                break
                        for element in layer.objects:
                            screen_chicken_x = element.rect.x - self._scroll_position * element.layer_speed
                            screen_chicken_y = element.rect.y
                            if pygame.Rect(screen_chicken_x, screen_chicken_y, element.rect.width,
                                           element.rect.height).collidepoint(aim_x, aim_y):
                                element.play(0.6)
                                element.shoot()
                                text = element.score
                                if text:
                                    self._kill_scores.append(TextKillWriter(
                                        element.rect.x - self._scroll_position * element.layer_speed,
                                        element.rect.top+10,
                                        str(text),
                                        BASIC_FONT,
                                        SCORE_TEXT_SIZE,
                                        BASIC_COLOR
                                    ))
                                self._update_kill_points(int(text))
                                break
                else:
                    self._sound_player.set_sound(EMPTY_CLIP_EFFECT)
                    self._sound_player.play(0.6)

        return None
