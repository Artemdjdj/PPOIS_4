from enum import Enum
from typing import Set, Optional
from src.utils.descriptor import NumberValidator
from src.exceptions.exceptions import GrillDoesNotExist, PositionError
from src.main.settings import AMOUNT_OF_FERTILIZER
from src.core.soil import Soil, SoilType
from src.core.plant import IPlant
from src.core.tool import ITool
from src.core.irrigation_system import IrrigationSystem


class MeatType(Enum):
    BEEF = ("говядина", 120)
    PORK = ("свинина", 90)
    CHICKEN = ("курица", 60)
    LAMB = ("баранина", 100)
    TURKEY = ("индейка", 80)
    VEAL = ("телятина", 75)
    DUCK = ("утка", 70)
    RABBIT = ("крольчатина", 60)
    GOAT = ("козлятина", 90)
    VENISON = ("оленина", 100)
    MUTTON = ("баранина", 110)
    GOOSE = ("гусятина", 90)

    @property
    def name(self) -> str:
        return self.value[0]

    @property
    def cooking_time(self) -> int:
        return self.value[1]


class BasicObject:
    squre = NumberValidator()
    perimeter = NumberValidator()

    def __init__(self, square: int | float, perimeter: int | float) -> None:
        self.square: int | float = square
        self.perimeter: int | float = perimeter


class Grill:
    def fry(self, meat: MeatType) -> str:
        return f"мясо приготовилось за {meat.cooking_time} минут"

    def __str__(self) -> str:
        return "Гриль для приготовления мясных блюд"


class RecreationArea(BasicObject):
    def __init__(self, square: int | float, perimeter: int | float) -> None:
        super().__init__(square, perimeter)
        self.__decorative_fittings: Set[str] = set()
        self.__grill: Optional[Grill] = None
        self.__is_clean = True

    def get_decorative_fittings(self) -> Set[str]:
        return self.__decorative_fittings

    def add_decorative_fitting(self, fitting: str) -> None:
        self.__decorative_fittings.add(fitting)

    def remove_decorative_fitting(self, fitting: str) -> None:
        self.__decorative_fittings.remove(fitting)

    def put_grill(self) -> bool:
        if self.__grill is None:
            self.__grill = Grill()
            self.__is_clean = False
            return True
        return False

    def remove_grill(self) -> bool:
        if self.__grill is not None:
            self.__grill = None
            return True
        return False

    def use_grill(self) -> str:
        if self.__grill:
            return self.__grill.fry()
        raise GrillDoesNotExist("Гриль не установлен!")

    @property
    def is_clean(self) -> bool:
        return self.__is_clean

    def clean(self) -> None:
        if not self.__is_clean:
            self.__is_clean = True


class GardenPlot(BasicObject):
    def __init__(
        self,
        square: int | float,
        perimeter: int | float,
        soil_type: SoilType,
        amount_of_all_water: int | float,
    ) -> None:
        super().__init__(square, perimeter)
        self.__soil: Soil = Soil(soil_type)
        self.__recreation_area: Optional[RecreationArea] = None
        self.__plants: list[IPlant] = []
        self.__tools: list[ITool] = []
        self.__irrigation_system: IrrigationSystem = IrrigationSystem(
            amount_of_all_water
        )

    def plant_plant(self, plant: IPlant) -> None:
        self.__plants.append(plant)

    @property
    def plants(self) -> list[IPlant]:
        return self.__plants

    def remove_plant(self, position: int) -> None:
        if not isinstance(position, int):
            raise TypeError("Некорректный формат номера растения")
        if abs(position) >= len(self.__plants):
            raise PositionError("Некорректая позиция растения")
        self.__plants.pop(position)

    def clear_garden_of_all_plants(self) -> None:
        self.__plants.clear()

    def water_plants(self, amount: int | float) -> None:
        self.__irrigation_system.turn_on()
        self.__irrigation_system.water(amount, self.__plants)
        self.__irrigation_system.turn_of()

    def fertilize_soil(self, amount_of_fertilizer: int | float)->None:
        coeff_fertilizer = amount_of_fertilizer/AMOUNT_OF_FERTILIZER
        self.__soil.fertilize(coeff_fertilizer)

