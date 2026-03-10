import json
from abc import ABC, abstractmethod
from typing import List, Tuple, Any


class BasicLeadersLoader(ABC):
    @abstractmethod
    def load(self)->List[Tuple[int, str, int]]:
        pass


class JsonLeadersLoader(BasicLeadersLoader):
    def __init__(self, path: str):
        self._path = path
        self._leaders = []

    def load(self)-> List[Tuple[int, str, int]]:
        with open(self._path, "r", encoding="utf-8") as file:
            data = json.load(file)

        for leader in data:
            self._leaders.append((int(leader["number"]), leader["name"], int(leader["record"])))

        return self._leaders