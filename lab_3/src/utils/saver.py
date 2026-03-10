import json
from abc import ABC, abstractmethod
from typing import List, Tuple, Any


class BasicPlayerSaver(ABC):
    @abstractmethod
    def save(self) -> None:
        pass


class JsonPlayerSaver(BasicPlayerSaver):
    def __init__(self, path: str, leaders: List[Tuple[int, str, int]]) -> None:
        self._path = path
        self._leaders = leaders

    def save(self) -> None:
        result_leaders = []
        for leader in self._leaders:
            result_leaders.append({"number": leader[0], "name": leader[1], "record": leader[2]})

        with open(self._path, "w", encoding="utf-8") as f:
            json.dump(result_leaders, f, indent=4)
