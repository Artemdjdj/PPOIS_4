from typing import List

from src.interface.cartridge import Cartridge


class CartridgesFactory:
    def __init__(self, max_count: int, start_x: int, start_y: int, space_between: int) -> None:
        self.max_count = max_count
        self._cartridges = []
        self._start_x = start_x
        self._start_y = start_y
        self._space_between = space_between

        self.create()

    @property
    def cartridges(self) -> List[Cartridge]:
        return self._cartridges

    def create(self) -> None:
        for i in range(self.max_count):
            self._cartridges.append(
                Cartridge(self._start_x - i * self._space_between, self._start_y, 0))


    def delete(self):
        if self._cartridges:
            self._cartridges.pop()