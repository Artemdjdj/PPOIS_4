import sys
import time

import pygame
from keyboard import restore_state

from src.interface.game import Game
from src.interface.game_over_screen import GameOverScreen
from src.interface.help_menu import HelpMenu
from src.interface.input_screen import NameInputScreen
from src.interface.menu import Menu
from src.interface.table_of_records import TableRecords
from src.settings.settings import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_NAME, BACKGROUND_COLOR, \
    MENU_MUSIC, GAME_MUSIC, FPS, FILE_TABLE_LEADERS, TIME_OF_SPAWN_CHICKENS, WIN_MUSIC, GAME_TIME
from src.settings.state import State
from src.objects.chicken import SittingChicken
from src.utils.loader import JsonLeadersLoader
from src.utils.saver import JsonLeadersSaver
from src.utils.timer import GameTimer


class Moorhuhn:
    def __init__(self) -> None:
        pygame.init()
        self._screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_NAME)
        self._loader = JsonLeadersLoader(FILE_TABLE_LEADERS)
        self._leaders = self._loader.load()
        self._state = State.MENU
        self._menu = Menu(self._screen)
        self._help_menu = HelpMenu(self._screen)
        self._table_records = TableRecords(self._screen, self._leaders)

        self._clock = pygame.time.Clock()
        self._dt = self._clock.tick(FPS) / 1000.0

        self._game = Game(self._screen, self._dt)
        self._create_chickens()

        self._spawn_timer = None
        self._timer = None

        self._play_music(MENU_MUSIC)

        self._create_timer()

    def _reset(self) -> None:
        self._create_timer()
        self._game.reset()
        self._create_chickens()

    def _play_music(self, name: str, volume: float = 0.2, is_infinity=True) -> None:
        pygame.mixer.music.load(name)
        pygame.mixer.music.set_volume(volume)
        if is_infinity:
            pygame.mixer.music.play(-1)

    def _create_chickens(self) -> None:
        self._game.create_moving_chickens_field((4, 6))
        self._game.create_sitting_chickens_game(10)
        self._game.create_flying_chickens(10)

    def _create_timer(self) -> None:
        self._timer = GameTimer(GAME_TIME)
        self._spawn_timer = time.time()

    def _check_leader(self, score: int):
        if score > self._leaders[0][1]:
            for i in range(len(self._leaders) - 1, 0, -1):
                self._leaders[i] = self._leaders[i - 1]

            self._play_music(WIN_MUSIC)
            name_input = NameInputScreen(self._screen, self._game.total_kill_points)
            player_name = name_input.run()
            self._leaders[0] = (player_name, score)

            saver = JsonLeadersSaver(FILE_TABLE_LEADERS, self._leaders)
            saver.save()
        else:
            self._play_music(MENU_MUSIC)
            game_over = GameOverScreen(self._screen, self._game.total_kill_points)
            game_over.run()

        self._reset()
        self._state = State.MENU

    def _draw_background(self):
        self._screen.fill(BACKGROUND_COLOR)

    def run_game(self) -> None:
        current_music = MENU_MUSIC
        while True:
            self._dt = self._clock.tick(FPS) / 1000.0
            new_state = None

            if self._state == State.MENU:
                self._menu.draw()
                pygame.mouse.set_visible(True)
                new_state = self._menu.check_event()
                if current_music != MENU_MUSIC:
                    current_music = MENU_MUSIC
                    self._play_music(MENU_MUSIC)

            elif self._state == State.PLAY:
                self._timer.update(self._dt)
                current_time = time.time()
                if current_time - self._spawn_timer > TIME_OF_SPAWN_CHICKENS:
                    self._game.spawn_chickens()
                    self._spawn_timer = current_time
                pygame.mouse.set_visible(False)
                if self._timer.is_finished():
                    self._state = State.CHECK_LEADER
                else:
                    self._game.update_time(str(self._timer.get_time_left()))
                    self._game.update_dt(self._dt)
                    self._game.draw()
                    new_state = self._game.check_event()
                    if current_music != GAME_MUSIC:
                        current_music = GAME_MUSIC
                        self._play_music(GAME_MUSIC)

            elif self._state == State.CHECK_LEADER:
                self._check_leader(self._game.total_kill_points)

            elif self._state == State.RECORD_TABLE:
                self._table_records.draw()
                new_state = self._table_records.check_event()

            elif self._state == State.HELP:
                self._help_menu.draw()
                new_state = self._help_menu.check_event()

            elif self._state == State.QUIT:
                sys.exit()

            if new_state is not None:
                self._state = new_state
            pygame.display.flip()
