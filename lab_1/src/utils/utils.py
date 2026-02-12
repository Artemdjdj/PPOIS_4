from enum import Enum
from src.utils.validator import ColorValidator


class ColorType(Enum):
    GREEN = "зеленый"
    BLUE = "голубой"
    BROWN = "коричневый"
    BLACK = "черный"
    YELLOW = "желтый"
    RED = "красный"
    ORANGE = "оранжевый"


class Color:
    def __init__(self) -> None:
        self.__color: str = None
        self.__validator = None

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str) -> None:
        self.__validator = ColorValidator(color)
        self.__validator.validate()
        self.__color = color
