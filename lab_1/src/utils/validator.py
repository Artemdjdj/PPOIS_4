from abc import ABC, abstractmethod
from enum import Enum
from src.exceptions.exceptions import (
    PositionError,
    ColorError,
    TypeOfSoilError,
)


class IValidator(ABC):
    @abstractmethod
    def validate(self) -> None:
        pass


class PositionValidator(IValidator):
    def __init__(self, len_of_arr: int, position: int) -> None:
        self.__len_of_arr = len_of_arr
        self.__position = position

    def validate(self):
        if not isinstance(self.__position, int):
            raise TypeError("Некорректный формат позиции в списке")
        if abs(self.__position) >= self.__len_of_arr:
            raise PositionError("Некорректая позиция")

class ColorType(Enum):
    GREEN = "зеленый"
    BLUE = "голубой"
    BROWN = "коричневый"
    BLACK = "черный"
    YELLOW = "желтый"
    RED = "красный"
    ORANGE = "оранжевый"

class ColorValidator(IValidator):
    def __init__(self, color: str) -> None:
        self.__color = color

    def validate(self):
        if not isinstance(self.__color, str):
            raise ValueError("цвет должен быть строкой")
        for color in ColorType:
            if color.value == self.__color:
                return
        raise ColorError("Некорректный цвет")

class SoilType(Enum):
    CLAY = "глинистая"
    SANDY = "песчаная"
    LOAMY = "суглинистая"
    PEATY = "торфяная"
    CHALKY = "известковая"
    CHERNOZEM = "чернозём"


class SoilValidator(IValidator):
    def __init__(self, type_of_soil: str) -> None:
        self.__type_of_soile = type_of_soil

    def validate(self):
        if not isinstance(self.__type_of_soil, str):
            raise ValueError("Тип почвы должен быть строкой")
        for soil in SoilType:
            if soil.value == self.__type_of_soil:
                return
        raise TypeOfSoilError("Некорректный тип почвы")
