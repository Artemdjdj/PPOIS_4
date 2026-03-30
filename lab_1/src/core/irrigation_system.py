import time
from typing import Dict, Any, List

from core.plant import Plant
from src.exceptions.exceptions import (
    SystemIsNotActiveError,
    LackOfWaterError,
    TooMuchPlantsAreWateredError,
)
from src.utils.descriptor import NumberValidator
MIN_TIME_OF_WATERING = 36000

class IrrigationSystem:

    def __init__(self) -> None:
        self.__is_active = False
        self.time_of_last_adding_water = None


    def water(self,plants: List[Plant]) -> None:
        if not self.__is_active:
            raise SystemIsNotActiveError("Система автоматического полива не включена")

        if not self.time_of_last_adding_water or time.time() - self.time_of_last_adding_water >= MIN_TIME_OF_WATERING:
            self.time_of_last_adding_water = time.time()
            for plant in plants:
                plant.water(self.time_of_last_adding_water)
            self.__is_active = False

        else:
            raise TooMuchPlantsAreWateredError("Растения недавно были политы, нужно что бы прошло время")

    def turn_on(self) -> None:
        self.__is_active = True

    def turn_of(self) -> None:
        self.__is_active = False

    def create_dict(self) -> Dict[str, Any]:
        return {
            "time_of_last_adding_water": self.time_of_last_adding_water,
        }

    @classmethod
    def create_object_from_dict(cls, data: Dict[str, Any]) -> 'IrrigationSystem':
        irrigation_system = cls()
        irrigation_system.__is_active = False
        irrigation_system.time_of_last_adding_water = data["time_of_last_adding_water"]
        return irrigation_system
