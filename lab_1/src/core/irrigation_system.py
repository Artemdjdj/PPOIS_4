from src.exceptions.exceptions import SystemIsNotActiveError, LackOfWaterError, TooMuchPlantsAreWateredError
from src.utils.descriptor import NumberValidator
from src.core.plant import Plant

class IrrigationSystem:
    amount_of_all_water = NumberValidator()

    def __init__(self, amount_of_all_water: int|float) -> None:
        self.__is_active = False
        self.amount_of_all_water: int | float = amount_of_all_water

    def water(self, amount: int | float, plants:list[Plant]) -> None:
        if not self.__is_active:
            raise SystemIsNotActiveError("Система автоматического полива не включена")
        if amount > self.amount_of_all_water:
            raise LackOfWaterError(
                "В системе автоматического полива нехватает воды залейте воду в бак"
            )
        count_of_watered_plants = sum(1 for plant in plants if plant.is_watered)
        if count_of_watered_plants > len(plants)//2:
            raise TooMuchPlantsAreWateredError(" Большая часть растений уже полита")
        for plant in plants:
            plant.is_watered = True
        self.amount_of_all_water -= amount

    def turn_on(self) -> None:
        self.__is_active = True

    def turn_of(self) -> None:
        self.__is_active = False