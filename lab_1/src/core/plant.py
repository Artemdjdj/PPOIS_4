import time
from typing import Optional, Dict, Any
from src.utils.descriptor import NumberValidator
from src.main.settings import MAX_HEIGHT_PLANT,MAX_DIAMETER_OF_PLANT
from src.utils.validator import ColorValidator, ColorType
from datetime import datetime, timezone

MIN_TIME_OF_WATERING = 10

class Color:
    def __init__(self) -> None:
        self.__color: Optional[str] = None
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
    height = NumberValidator(MAX_HEIGHT_PLANT)
    diameter = NumberValidator(MAX_DIAMETER_OF_PLANT)

    def __init__(
        self,
        height: int | float,
        name: str,
        color: Color,
        is_watered: bool = False,
        diameter: int | float = 0,
    ) -> None:
        self.height = height
        self.__name = name
        self.__color = color
        self.diameter = diameter
        self.is_watered = is_watered
        self.__time_of_last_adding_water: Optional[datetime] = None

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def time_of_last_adding_water(self) -> Optional[datetime]:
        current_time = datetime.now(timezone.utc).replace(tzinfo=None)
        if self.__time_of_last_adding_water is not None and \
           (current_time - self.__time_of_last_adding_water).total_seconds() >= MIN_TIME_OF_WATERING:
            self.__time_of_last_adding_water = None
            self.is_watered = False
        return self.__time_of_last_adding_water

    @time_of_last_adding_water.setter
    def time_of_last_adding_water(self, dt: Optional[datetime]) -> None:
        if dt is not None:
            if dt.tzinfo is not None:
                dt = dt.astimezone(timezone.utc).replace(tzinfo=None)
        self.__time_of_last_adding_water = dt

    def water(self, my_time: datetime) -> None:
        if my_time.tzinfo is not None:
            my_time = my_time.astimezone(timezone.utc).replace(tzinfo=None)
        self.is_watered = True
        self.__time_of_last_adding_water = my_time

    @property
    def color(self) -> str:
        return self.__color.color

    def __str__(self) -> str:
        is_watered = "полито" if self.is_watered else "не полито"
        return f"Растение {self.__name}, высота которого: {self.height}, {is_watered}"

    def create_dict(self) -> Dict[str, Any]:
        return {
            "height": self.height,
            "name": self.__name,
            "color": self.color,
            "is_watered": self.is_watered,
            "diameter": self.diameter,
            "time_of_last_adding_water": self.__time_of_last_adding_water.isoformat() if self.__time_of_last_adding_water else None,
        }

    @classmethod
    def create_object_from_dict(cls, info_dict: Dict[str, Any]) -> "Plant":
        color_obj = Color()
        color_obj.color = info_dict["color"]
        plant = cls(
            height=info_dict["height"],
            name=info_dict["name"],
            color=color_obj,
            is_watered=info_dict["is_watered"],
            diameter=info_dict["diameter"],
        )
        if info_dict.get("time_of_last_adding_water"):
            dt = datetime.fromisoformat(info_dict["time_of_last_adding_water"])
            plant.time_of_last_adding_water = dt
        else:
            plant.time_of_last_adding_water = None
        return plant

    def update(self) -> None:
        _ = self.time_of_last_adding_water

    def update_time_of_last_adding_water(self) -> None:
        current_time = datetime.now(timezone.utc).replace(tzinfo=None)
        if (self.__time_of_last_adding_water is None or
            (current_time - self.__time_of_last_adding_water).total_seconds() >= MIN_TIME_OF_WATERING):
            self.water(current_time)