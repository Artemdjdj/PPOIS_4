# src/screens/name_input_screen.py

import pygame

from src.interface.mixins.end_screen import EndScreen
from src.settings.settings import (
    BACKGROUND_INPUT_NAME, CONFIRM_NAME_TEXT, INPUT_NAME_TEXT,
    NEW_RECORD_TEXT, MAX_LENGTH_NAME, WIDTH_INPUT_BOX, HEIGHT_INPUT_BOX,
    BASIC_COLOR, BASE_NAME, BASE_SYMBOL_IN_INPUT
)


class NameInputScreen(EndScreen):
    def __init__(self, screen, score: int, max_length: int = MAX_LENGTH_NAME, prompt: str = INPUT_NAME_TEXT) -> None:
        super().__init__(screen, score, NEW_RECORD_TEXT, bg_image=BACKGROUND_INPUT_NAME)

        self.max_length = max_length
        self.prompt = prompt
        self.input_text = ""

        self.input_rect = pygame.Rect(
            screen.get_width() // 2 - 150,
            screen.get_height() // 2 + 150,
            WIDTH_INPUT_BOX, HEIGHT_INPUT_BOX
        )

    def _handle_custom_events(self, events) -> None:
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.input_text = self.input_text[:-1]
                elif (event.key != pygame.K_RETURN
                      and event.unicode.isprintable()
                      and len(self.input_text) < self.max_length):
                    self.input_text += event.unicode

    def draw(self) -> None:
        self._draw_background()
        self._draw_title()
        self._draw_prompt()
        self._draw_input_box()
        self._draw_exit_hint()
        pygame.display.flip()

    def _draw_exit_hint(self) -> None:
        surf = self.font_small.render(CONFIRM_NAME_TEXT, True, BASIC_COLOR)
        rect = surf.get_rect(center=(
            self.screen.get_width() // 2,
            self.screen.get_height() - 40
        ))
        self.screen.blit(surf, rect)

    def _draw_prompt(self) -> None:
        surf = self.font_small.render(self.prompt, True, BASIC_COLOR)
        rect = surf.get_rect(center=(
            self.screen.get_width() // 2,
            self.screen.get_height() // 2 + 100
        ))
        self.screen.blit(surf, rect)

    def _draw_input_box(self) -> None:
        pygame.draw.rect(self.screen, BASIC_COLOR, self.input_rect, 2)

        display_text = self.input_text + BASE_SYMBOL_IN_INPUT
        surf = self.font_small.render(display_text, True, BASIC_COLOR)
        text_rect = surf.get_rect(
            midleft=(self.input_rect.x + 5, self.input_rect.centery)
        )

        if text_rect.width > self.input_rect.width - 10:
            surf = self.font_small.render(self.input_text, True, BASIC_COLOR)
            text_rect = surf.get_rect(
                midleft=(self.input_rect.x + 5, self.input_rect.centery)
            )

        self.screen.blit(surf, text_rect)

    def run(self) -> str:
        super().run()
        return self.input_text if self.input_text else BASE_NAME
