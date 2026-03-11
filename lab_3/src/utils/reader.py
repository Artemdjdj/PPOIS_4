import json
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


class BasicReader(ABC):
    def __init__(self, path: str|Path):
        self._path = path

    @property
    def path(self) -> str|Path:
        return self._path

    @path.setter
    def path(self, path: str|Path) -> None:
        self._path = path

    @abstractmethod
    def read(self) -> Any:
        pass


class TxtReader(BasicReader):
    def read(self) -> Any:
        with open(self._path, 'r') as f:
            text = f.read()
        return text


class JsonReader(BasicReader):
    def read(self) -> Any:
        with open(self._path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
