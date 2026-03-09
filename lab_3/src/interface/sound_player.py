import pygame

class SoundPlayer:
    def __init__(self):
        self._player = None

    def set_sound(self, sound:str)->None:
        self._player = pygame.mixer.Sound(sound)

    def play(self, volume:float) -> None:
        if self._player:
            self._player.set_volume(volume)
            self._player.play()