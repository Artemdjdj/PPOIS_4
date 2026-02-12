from src.utils.descriptor import NumberValidator
from src.utils.utils import Color
from src.main.settings import MAX_DIAMETER_OF_PLANT


class Plant:
    height = NumberValidator()
    diameter = NumberValidator(MAX_DIAMETER_OF_PLANT)

    def __init__(
        self,
        height: int | float,
        name: str,
        color: Color,
        is_watered: bool = False,
        diameter: int | float = None,
    ) -> None:
        self.height = height
        self.__name = name
        self.__color = color
        self.__is_watered = is_watered
        self.diameter = diameter

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def color(self) -> str:
        return self.__color.name

    @property
    def is_watered(self) -> bool:
        return self.__is_watered

    @is_watered.setter
    def is_watered(self, is_watered) -> None:
        self.__is_watered = is_watered

    def __str__(self)->str:
        return f"{self.__name} and height {self.__height}"
