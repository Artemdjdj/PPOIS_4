import pygame

from typing import Callable, Any


class Button:
    def __init__(self, coordinate_x:int, coordinate_y:int, width:int, height:int, color:tuple,background_color:tuple, background_hover_color:tuple, text:str, font:pygame.font.Font, screen:Any,func:Callable[[], None]):
        self._rect = pygame.Rect(coordinate_x,coordinate_y, width, height)
        self._color = color
        self._background_color = background_color
        self._background_hover_color = background_hover_color
        self._text = text
        self._font = font
        self._func = func
        self._screen = screen

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        if self._rect.collidepoint(mouse_pos):
            pygame.draw.rect(self._screen, self._background_hover_color, self._rect)
        else:
            pygame.draw.rect(self._screen, self._background_color, self._rect)

        res_label = self._font.render(self._text, True, self._color)
        label_rect = res_label.get_rect(center=self._rect.center)
        self._screen.blit(res_label, label_rect)


    def check_event(self, event:pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self._rect.collidepoint(event.pos):
                self._func()