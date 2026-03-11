# src/screens/base_screen.py

import pygame
import sys

from src.settings.settings import (
    FPS, BASIC_FONT, DEFAULT_BACKGROUND, BASIC_COLOR,
    FONT_LARGE_SIZE, FONT_INPUT_SIZE, NAME_POINT, CONFIRM_NAME_TEXT, CONTINUE_TEXT
)


class EndScreen:
    def __init__(self, screen, score:int, title, bg_image=None):
        self.screen = screen
        self.score = score
        self.title = title
        self.bg_color = DEFAULT_BACKGROUND
        self.active = True

        self.font_large = pygame.font.Font(BASIC_FONT, FONT_LARGE_SIZE)
        self.font_small = pygame.font.Font(BASIC_FONT, FONT_INPUT_SIZE)
        self.font_input = pygame.font.Font(BASIC_FONT, FONT_INPUT_SIZE)

        self.background = None
        if bg_image:
            try:
                raw = pygame.image.load(bg_image).convert()
                self.background = pygame.transform.scale(
                    raw, (screen.get_width(), screen.get_height())
                )
            except pygame.error:
                self.background = None

    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.active = False
        self._handle_custom_events(events)

    def _handle_custom_events(self, events):
        pass

    def draw(self):
        self._draw_background()
        self._draw_title()
        self._draw_exit_hint()
        pygame.display.flip()

    def _draw_background(self):
        if self.background:
            self.screen.blit(self.background, (0, 0))
        else:
            self.screen.fill(self.bg_color)

    def _draw_title(self):
        surf = self.font_large.render(self.title + f" {self.score} {NAME_POINT}", True, BASIC_COLOR)
        rect = surf.get_rect(center=(
            self.screen.get_width() // 2,
            self.screen.get_height() // 2 + 50
        ))
        self.screen.blit(surf, rect)

    def _draw_exit_hint(self):
        surf = self.font_small.render(CONTINUE_TEXT, True, BASIC_COLOR)
        rect = surf.get_rect(center=(
            self.screen.get_width() // 2,
            self.screen.get_height() - 220
        ))
        self.screen.blit(surf, rect)

    def run(self):
        clock = pygame.time.Clock()
        while self.active:
            clock.tick(FPS)
            self.handle_events()
            self.draw()