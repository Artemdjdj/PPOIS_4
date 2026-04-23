import time
from typing import Dict, Any, List, Optional
from datetime import datetime, timezone

from src.core.plant import Plant
from src.exceptions.exceptions import (
    SystemIsNotActiveError,
    TooMuchPlantsAreWateredError,
)

MIN_TIME_OF_WATERING = 10

class IrrigationSystem:
    def __init__(self) -> None:
        self.__is_active = False
        self._time_of_last_adding_water: Optional[datetime] = None

    @property
    def time_of_last_adding_water(self) -> Optional[datetime]:
        return self._time_of_last_adding_water

    @time_of_last_adding_water.setter
    def time_of_last_adding_water(self, value: Optional[datetime]) -> None:
        if value is not None and value.tzinfo is not None:
            value = value.astimezone(timezone.utc).replace(tzinfo=None)
        self._time_of_last_adding_water = value

    def water(self, plants: List[Plant]) -> str:
        if not self.__is_active:
            raise SystemIsNotActiveError("Система автоматического полива не включена")

        if len(plants) == 0:
            raise ValueError("У вас нет растений, прежде чем включить полив, добавьте растения")

        current_time = datetime.now(timezone.utc).replace(tzinfo=None)
        last_time = self._time_of_last_adding_water

        if last_time is None or (current_time - last_time).total_seconds() >= MIN_TIME_OF_WATERING:
            self._time_of_last_adding_water = current_time
            for plant in plants:
                plant.water(current_time)
            self.__is_active = False
            return "Растения не политы, вы можете включить систему полива, которая автоматически польет все растения"
        else:
            raise TooMuchPlantsAreWateredError("Растения недавно были политы, нужно чтобы прошло время (10 секунд минимум)")

    def turn_on(self) -> None:
        self.__is_active = True

    def turn_of(self) -> None:  
        self.__is_active = False

    @property
    def is_active(self) -> bool:
        return self.__is_active

    def create_dict(self) -> Dict[str, Any]:
        return {"time_of_last_adding_water": self._time_of_last_adding_water.isoformat() if self._time_of_last_adding_water else None}

    @classmethod
    def create_object_from_dict(cls, data: Dict[str, Any]) -> 'IrrigationSystem':
        system = cls()
        val = data.get("time_of_last_adding_water")
        if isinstance(val, str):
            system._time_of_last_adding_water = datetime.fromisoformat(val)
        else:
            system._time_of_last_adding_water = None
        system.__is_active = False
        return system