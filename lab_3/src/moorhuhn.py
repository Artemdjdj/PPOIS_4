import sys

import pygame
from keyboard import restore_state

from src.interface.game import Game
from src.interface.help_menu import HelpMenu
from src.interface.menu import Menu
from src.interface.table_of_records import TableRecords
from src.settings.settings import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_NAME, BACKGROUND_COLOR, \
    MENU_MUSIC, GAME_MUSIC, FPS, FILE_TABLE_LEADERS
from src.settings.state import State
from src.objects.chicken import SittingChicken
from src.utils.loader import JsonLeadersLoader
from src.utils.saver import JsonLeadersSaver
from src.utils.timer import GameTimer


class Moorhuhn:
    """Класс для управлением ресурсами и поведением игры"""

    def __init__(self)->None:
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
        self._game.create_sitting_chickens_field((20,15))
        self._game.create_sitting_chickens_game(20)
        self._game.create_flying_chickens(10)

        pygame.mixer.music.load(MENU_MUSIC)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

        self._timer = GameTimer(90.0)

    def _check_leader(self, score:int):
        res_pos = -1
        res_leader = None
        for i, leader in enumerate(self._leaders):
            if score > leader[1]:
                res_pos = i
                res_leader = leader
                break

        print("All right")
        if res_leader is None:
            self._state = State.GAME_OVER
        else:
            print("ok")
            self._leaders[res_pos] = ("Dima babnik", score)
            saver = JsonLeadersSaver(FILE_TABLE_LEADERS, self._leaders)
            saver.save()
            sys.exit()

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
                    pygame.mixer.music.load(MENU_MUSIC)
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.2)

            elif self._state == State.PLAY:
                self._timer.update(self._dt)
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
                        pygame.mixer.music.load(GAME_MUSIC)
                        pygame.mixer.music.play(-1)
                        pygame.mixer.music.set_volume(0.2)

            elif self._state == State.CHECK_LEADER:
                self._check_leader(self._game.total_kill_points)

            elif self._state == State.GAME_OVER:
                print("game over")
                sys.exit()

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

