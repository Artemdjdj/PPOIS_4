import sys
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
    EMPTY_CLIP_EFFECT, RELOAD_CLIP_EFFECT, RELOAD_TEXT_SIZE, RELOAD_TEXT_COLOR, RELOAD_CLIP_TEXT, SCORE_TEXT_SIZE, \
    SCORE_TEXT, TIME_TEXT, SPACE_SCORE_X, SPACE_INFO_Y, SPACE_TIME_X, PUDDLE_COORD_X, PUDDLE_COORD_Y
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

        self._layer_game.add_object(Car(CAR_COORD_X, CAR_COORD_Y, SPEED_THIRD_LAYER))
        self._layer_game.add_object(Puddle(PUDDLE_COORD_X, PUDDLE_COORD_Y, SPEED_THIRD_LAYER))
        self._layer_game.add_object(Oven(OVEN_COORD_X, OVEN_COORD_Y, SPEED_THIRD_LAYER))
        self._layer_game.add_object(Hedgehog(HEDGEHOG_COORD_X, HEDGEHOG_COORD_Y, SPEED_THIRD_LAYER))

        self._layer_sky.add_object(Balloon(BALLOON_COORD_X, BALLOON_COORD_Y, SPEED_THIRD_LAYER))
        self._layer_field.add_object(Toilet(TOILET_COORD_X, TOILET_COORD_Y, SPEED_SECOND_LAYER))

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

    def create_sitting_chickens_game(self, count: int):
        self._layer_game.create_chickens(count)

    def create_sitting_chickens_field(self, counts: Tuple[int, int]):
        self._layer_field.create_chickens(counts)

    def create_flying_chickens(self, count: int):
        self._layer_sky.create_chickens(count)

    def update_time(self, time:str)->None:
        self._time_text.set_text(time)

    def update(self, dt: float) -> None:
        self._dt = dt

    def draw(self) -> None:
        for x in range(3):
            self._layer_sky.draw(self._screen, x, self._scroll_position)
            self._layer_field.draw(self._screen, x, self._scroll_position)
            self._layer_game.draw(self._screen, x, self._scroll_position)

        # for chicken in self._layer_sky.chickens:
        #     chicken.update(self._dt)

        for layer in self._layers:
            for element in layer.objects:
                element.animate()
                element.draw(self._screen, self._scroll_position)

            for chicken in layer.chickens:
                chicken.update(self._dt)
                chicken.animate()
                chicken.draw(self._screen, self._scroll_position)

        self._score_text.draw(self._screen)
        self._time_text.draw(self._screen)

        if self._clip.cartridges:
            for cartridge in self._clip.cartridges:
                cartridge.draw(self._screen, self._scroll_position)
        else:
            self._reload_clip_text.draw(self._screen)

        self._cursor.draw(self._screen)

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
                                break
                        for element in layer.objects:
                            screen_chicken_x = element.rect.x - self._scroll_position * element.layer_speed
                            screen_chicken_y = element.rect.y
                            if pygame.Rect(screen_chicken_x, screen_chicken_y, element.rect.width,
                                           element.rect.height).collidepoint(aim_x, aim_y):
                                element.play(0.6)
                                element.shoot()
                                break


                    # for layer in self._layers:
                    #     for chicken in layer.chickens:
                    #         screen_chicken_x = chicken.rect.x - self._scroll_position * chicken.layer_speed
                    #         screen_chicken_y = chicken.rect.y
                    #         # if chicken.rect.collidepoint(aim_x, aim_y):
                    #         collision_rect = chicken.get_collision_rect()
                    #         collision_rect.x = screen_chicken_x
                    #         collision_rect.y = screen_chicken_y
                    #         if collision_rect.collidepoint(aim_x, aim_y):
                    #             chicken.kill()
                    #             break
                            # if pygame.Rect(screen_chicken_x, screen_chicken_y, chicken.rect.width, chicken.rect.height).collidepoint(
                            #         aim_x, aim_y):
                            #     chicken.kill()
                            #     break
                else:
                    self._sound_player.set_sound(EMPTY_CLIP_EFFECT)
                    self._sound_player.play(0.6)

        return None
