import pygame
import sys

from src.settings.settings import FPS, BASIC_FONT, BACKGROUND_INPUT_NAME, CONFIRM_NAME_TEXT, INPUT_NAME_TEXT, \
    NEW_RECORD_TEXT, MAX_LENGTH_NAME, WIDTH_INPUT_BOX, HEIGHT_INPUT_BOX, BASIC_COLOR, BASE_NAME, BASE_SYMBOL_IN_INPUT, \
    DEFAULT_BACKGROUND, FONT_LARGE_SIZE, FONT_INPUT_SIZE


class NameInputScreen:
    def __init__(self, screen, max_length=MAX_LENGTH_NAME, title=NEW_RECORD_TEXT,
                 prompt=INPUT_NAME_TEXT):
        self.screen = screen
        self.max_length = max_length
        self.title = title
        self.prompt = prompt
        self.bg_color = DEFAULT_BACKGROUND
        self.bg_image = BACKGROUND_INPUT_NAME
        self.font_large = pygame.font.Font(BASIC_FONT, FONT_LARGE_SIZE)
        self.font_small = pygame.font.Font(BASIC_FONT, FONT_INPUT_SIZE)
        self.font_input = pygame.font.Font(BASIC_FONT, FONT_INPUT_SIZE)

        self.input_rect = pygame.Rect(
            screen.get_width() // 2 - 150,
            screen.get_height() // 2 + 150,
            WIDTH_INPUT_BOX, HEIGHT_INPUT_BOX
        )
        self.input_text = ""
        self.active = True

        self.background = None
        if self.bg_image:
            try:
                self.background = pygame.image.load(self.bg_image).convert()
                self.background = pygame.transform.scale(self.background,
                                                         (screen.get_width(), screen.get_height()))
            except pygame.error:
                self.background = DEFAULT_BACKGROUND

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.input_text = self.input_text[:-1]
                else:
                    if event.unicode.isprintable() and len(self.input_text) < self.max_length:
                        self.input_text += event.unicode

    def draw(self):
        if self.background:
            self.screen.blit(self.background, (0, 0))
        else:
            self.screen.fill(self.bg_color)

        title_surf = self.font_large.render(self.title, True, BASIC_COLOR)
        title_rect = title_surf.get_rect(center=(self.screen.get_width() // 2,
                                                 self.screen.get_height() // 2 + 50))
        self.screen.blit(title_surf, title_rect)

        prompt_surf = self.font_small.render(self.prompt, True, BASIC_COLOR)
        prompt_rect = prompt_surf.get_rect(center=(self.screen.get_width() // 2,
                                                   self.screen.get_height() // 2 + 100))
        self.screen.blit(prompt_surf, prompt_rect)

        pygame.draw.rect(self.screen, BASIC_COLOR, self.input_rect, 2)

        display_text = self.input_text + BASE_SYMBOL_IN_INPUT
        text_surf = self.font_input.render(display_text, True, BASIC_COLOR)
        text_rect = text_surf.get_rect(midleft=(self.input_rect.x + 5, self.input_rect.centery))

        if text_rect.width > self.input_rect.width - 10:
            text_surf = self.font_input.render(self.input_text, True, BASIC_COLOR)
            text_rect = text_surf.get_rect(midleft=(self.input_rect.x + 5, self.input_rect.centery))

        self.screen.blit(text_surf, text_rect)

        inst_surf = self.font_small.render(CONFIRM_NAME_TEXT, True, BASIC_COLOR)
        inst_rect = inst_surf.get_rect(center=(self.screen.get_width() // 2,
                                               self.screen.get_height() // 2 + 220))
        self.screen.blit(inst_surf, inst_rect)

        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()
        while self.active:
            clock.tick(FPS)
            self.handle_events()
            self.draw()
        return self.input_text if self.input_text else BASE_NAME
