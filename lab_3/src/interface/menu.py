import sys
from typing import Optional

import pygame

from src.interface.button import Button
from src.settings.state import State
from src.settings.settings import SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT


class Menu:
    def __init__(self, screen:pygame.Surface)->None:
        self._screen = screen
        self._buttons = [
            Button(SCREEN_WIDTH//2-BUTTON_WIDTH//2, 190, BUTTON_WIDTH, BUTTON_HEIGHT, (255, 255, 255), (128, 0, 0), (200, 0, 0), "Играть",
                   pygame.font.Font("D:/PPOIS_4/lab_3/assets/fonts/main.otf", 20), State.PLAY),
            Button(SCREEN_WIDTH//2-BUTTON_WIDTH//2, 280, BUTTON_WIDTH, BUTTON_HEIGHT, (255, 255, 255), (128, 0, 0), (200, 0, 0), "Таблица лидеров",
                   pygame.font.Font("D:/PPOIS_4/lab_3/assets/fonts/main.otf", 20), State.RECORD_TABLE),
            Button(SCREEN_WIDTH//2-BUTTON_WIDTH//2, 370, BUTTON_WIDTH, BUTTON_HEIGHT, (255, 255, 255), (128, 0, 0), (200, 0, 0), "Справка",
                   pygame.font.Font("D:/PPOIS_4/lab_3/assets/fonts/main.otf", 20), State.HELP),
            Button(SCREEN_WIDTH//2-BUTTON_WIDTH//2, 460, BUTTON_WIDTH, BUTTON_HEIGHT, (255, 255, 255), (128, 0, 0), (200, 0, 0), "Выйти",
                   pygame.font.Font("D:/PPOIS_4/lab_3/assets/fonts/main.otf", 20), State.QUIT),
        ]
        self._background = pygame.image.load("D:/PPOIS_4/lab_3/assets/images/result_menu2.png").convert_alpha()
        self._background = pygame.transform.scale(self._background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self._screen.blit(self._background, (0, 0))

    def draw(self)->None:
        for button in self._buttons:
            button.draw(self._screen)

    def check_event(self)->Optional[State]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            for button in self._buttons:
                result = button.check_event(event)
                if result is not None:
                    return result
        return None



