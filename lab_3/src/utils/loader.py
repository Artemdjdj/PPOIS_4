import json
from abc import ABC, abstractmethod
from typing import List, Tuple, Any


class BasicLeadersLoader(ABC):
    @abstractmethod
    def load(self)->List[Tuple[str, int]]:
        pass


class JsonLeadersLoader(BasicLeadersLoader):
    def __init__(self, path: str):
        self._path = path
        self._leaders = []

    def load(self)-> List[Tuple[str, int]]:
        with open(self._path, "r", encoding="utf-8") as file:
            data = json.load(file)

        for leader in data:
            self._leaders.append((leader["name"], int(leader["record"])))

        self._leaders = sorted(self._leaders, key=lambda x: -x[1])
        return self._leaders