import json
from abc import ABC, abstractmethod
from typing import List, Tuple, Any


class BasicLeadersSaver(ABC):
    @abstractmethod
    def save(self) -> None:
        pass


class JsonLeadersSaver(BasicLeadersSaver):
    def __init__(self, path: str, leaders: List[Tuple[str, int]]) -> None:
        self._path = path
        self._leaders = leaders

    def save(self) -> None:
        result_leaders = []
        for leader in self._leaders:
            result_leaders.append({"name": leader[0], "record": leader[1]})

        with open(self._path, "w", encoding="utf-8") as f:
            json.dump(result_leaders, f, indent=4)
