from abc import ABC, abstractmethod


class BasicRulesReader(ABC):
    @abstractmethod
    def read(self)->str:
        pass

class TxtReader(BasicRulesReader):
    def __init__(self, path: str):
        self._path = path

    def read(self)->str:
        with open(self._path, 'r') as f:
            text = f.read()
            return text

