from enum import Enum
from datetime import date
from src.main.settings import COUNT_OF_WORK_HOURS_WORN, COUNT_OF_WORK_HOURS_BROKEN


class ToolState(Enum):
    PERFECT = "идеальное"
    GOOD = "хорошее"
    WORN = "поврежденное"
    BROKEN = "сломанное"


class Tool:
    def __init__(self, name: str, brand: str, description: str) -> None:
        self.__name: str = name
        self.__brand: str = brand
        self.__description: str = description
        self.__state: ToolState = ToolState.PERFECT
        self.__usage_count: int | float = 0
        self.__date_of_maintain: date = date.today()

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

    def __default_maintain(self, time_repair: int) -> None:
        self.__state: ToolState = ToolState.GOOD
        self.__usage_count: int | float = 0
        self.__date_of_maintain = date.today()

    def maintenance(self) -> str:
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

    def perform_task(self, work_hours: int | float) -> bool:
        self.__usage_count += work_hours
        if (
            self.__usage_count >= COUNT_OF_WORK_HOURS_WORN
            and self.__usage_count <= COUNT_OF_WORK_HOURS_BROKEN
        ):
            self.__state = ToolState.WORN
        elif self.__usage_count > COUNT_OF_WORK_HOURS_BROKEN:
            self.__state = ToolState.BROKEN

    def __str__(self) -> None:
        return f"Инструмент: {self.__name}, бренд: {self.__brand}"
