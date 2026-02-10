from typing import Any
from abc import ABC, abstractmethod
from enum import Enum
from datetime import date


class ToolState(Enum):
    PERFECT = "идеальное"
    GOOD = "хорошее"
    WORN = "поврежденное"
    BROKEN = "сломанное"


class Tool(ABC):
    def __init__(self, name: str, brand: str, description: str) -> None:
        self.__name = name
        self.__brand = brand
        self.__description = description
        self.__state = ToolState.PERFECT
        self.__usage_count = 0
        self.__date_of_maintain = date.today()

    @property
    def name(self) -> str:
        return self.__name

    @property
    def brand(self) -> str:
        return self.__brand

    @property
    def description(self) -> str:
        return self.__description

    @property
    def state(self) -> str:
        return self.__state.value

    @property
    def usage_count(self) -> str:
        return self.__usage_count

    @property
    def date_of_maintain(self) -> date:
        return self.__date_of_maintain

    def maintain(self) -> str:
        pass

    @abstractmethod
    def perform_task(self, work_hours: float):
        pass


class Shovel(Tool):
    def perform_task(self, **kwargs: Any):
        pass
