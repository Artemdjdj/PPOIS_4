from typing import Any
from abc import ABC, abstractmethod
from enum import Enum
from datetime import date
from src.main.settings import (
    COEFF_WEAR_SHOVEL,
    COEFF_WEAR_GARDEN_SHERAS,
    COEFF_WEAR_RAKE,
    SPECIAL_COEFF_OF_MAINTAIN,
    COEFF_OF_DIAMETER,
)


class ToolState(Enum):
    PERFECT = "идеальное"
    GOOD = "хорошее"
    WORN = "поврежденное"
    BROKEN = "сломанное"


class ITool(ABC):
    def __init__(self, brand: str, description: str) -> None:
        self.__brand: str = brand
        self.__description: str = description
        self.__state: ToolState = ToolState.PERFECT
        self.__usage_count: int | float = 0
        self.__date_of_maintain: date = date.today()

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

    def __default_maintain(self, time_repair: int) -> None:
        self.__state:ToolState = ToolState.GOOD
        self.__usage_count:int|float = 0
        self.__date_of_maintain = date.today()

    def maintain(self) -> str:
        if self.__state == ToolState.PERFECT:
            return "Инструмент новый, обслуживание не надо"
        elif self.__state == ToolState.GOOD:
            return "Инструмент в хорошем состоянии, можно приступать к работе"
        elif self.__state == ToolState.WORN:
            self.__default_maintain(1)
            return "Инструмент имел небольшие дефекты, теперь все готово инструмент и хорошем состоянии"
        else:
            self.__default_maintain(2)
            return "Инструмент был сильно поврежден, теперь все готово инструмент и хорошем состоянии"

    @abstractmethod
    def perform_task(self, work_hours: int | float, kwargs: Any) -> bool:
        pass


class Shovel(ITool):
    def perform_task(self, work_hours: int | float, **kwargs: Any) -> bool:
        self.__usage_count += work_hours / COEFF_WEAR_SHOVEL
        return self.__usage.count <= SPECIAL_COEFF_OF_MAINTAIN


class GardenSheras(ITool):
    def perform_task(self, work_hours: int | float, **kwargs: Any) -> bool:
        diameter = kwargs.get("diameter", None)
        if diameter:
            self.__usage_count += (
                work_hours * diameter / (COEFF_WEAR_GARDEN_SHERAS * COEFF_OF_DIAMETER)
            )
        else:
            self.__usage_count += work_hours / COEFF_WEAR_GARDEN_SHERAS
        return self.__usage.count <= SPECIAL_COEFF_OF_MAINTAIN


class Rake(ITool):
    def perform_task(self, work_hours: int | float, **kwargs: Any) -> bool:
        self.__usage_count += work_hours / COEFF_WEAR_RAKE
        return self.__usage.count <= SPECIAL_COEFF_OF_MAINTAIN
