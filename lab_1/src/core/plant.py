from typing import Optional, Dict, Any
from src.utils.descriptor import NumberValidator
from src.main.settings import MAX_DIAMETER_OF_PLANT
from src.utils.validator import ColorValidator, ColorType


class Color:
    def __init__(self) -> None:
        self.__color: Optional[ColorType] = None
        self.__validator = None

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str) -> None:
        color = color.lower()
        self.__validator = ColorValidator(color)
        self.__validator.validate()
        self.__color = color


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
        return self.__color.color

    @property
    def is_watered(self) -> bool:
        return self.__is_watered

    @is_watered.setter
    def is_watered(self, is_watered) -> None:
        self.__is_watered = is_watered

    def __str__(self) -> str:
        return f"Растение {self.__name} высота которого: {self.height}"

    def create_dict(self) -> Dict[str, Any]:
        return {
            "height": self.height,
            "name": self.__name,
            "color": self.color,
            "is_watered": self.__is_watered,
            "diameter": self.diameter,
        }

    @classmethod
    def create_object_from_dict(cls, info_dict: Dict[str, Any]) -> "Plant":
        color_obj = Color()
        color_obj.color = info_dict["color"]  # правильно
        return cls(
            height=info_dict["height"],
            name=info_dict["name"],
            color=color_obj,
            is_watered=info_dict["is_watered"],
            diameter=info_dict["diameter"],
        )
