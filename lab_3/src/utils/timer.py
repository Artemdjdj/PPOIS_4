import pygame


class GameTimer:
    def __init__(self, start_time: float):
        self.time_left = start_time
        self.finished = False

    def update(self, dt: float):
        if not self.finished:
            self.time_left -= dt
            if self.time_left <= 0:
                self.time_left = 0
                self.finished = True

    def get_time_left(self) -> int:
        return int(self.time_left)

    def is_finished(self) -> bool:
        return self.finished