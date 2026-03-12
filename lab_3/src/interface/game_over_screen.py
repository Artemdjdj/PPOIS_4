import pygame

from src.interface.mixins.end_screen import EndScreen
from src.settings.settings import BACKGROUND_INPUT_NAME, NAME_GAME_OVER


class GameOverScreen(EndScreen):
    def __init__(self, screen, score: int, bg_image=BACKGROUND_INPUT_NAME) -> None:
        super().__init__(screen, score, NAME_GAME_OVER, bg_image=bg_image)
