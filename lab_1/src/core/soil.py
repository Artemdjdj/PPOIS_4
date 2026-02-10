from enum import Enum
from src.utils.descriptor import NumberValidator
from src.exceptions.exceptions import TypeOfSoilError
from src.main.settings import MAX_COEFF


class SoilType(Enum):
    CLAY = "глинистая"
    SANDY = "песчаная"
    LOAMY = "суглинистая"
    PEATY = "торфяная"
    CHALKY = "известковая"
    CHERNOZEM = "чернозём"


class Soil:
    coeff_water = NumberValidator(MAX_COEFF)
    coeff_fertilizer = NumberValidator(MAX_COEFF)

    def __init__(self, coeff_water: int | float, coeff_fertilizer: int | float):
        self.__type_of_soil = SoilType.LOAMY
        self.coeff_water = coeff_water
        self.coeff_fertilizer = coeff_fertilizer

    @property
    def type_of_soil(self) -> str:
        return self.__type_of_soil.value

    @type_of_soil.setter
    def type_of_soil(self, type_of_soil: str) -> None:
        if not isinstance(type_of_soil, str):
            raise ValueError("Тип почвы должен быть строкой")
        type_of_soil = type_of_soil.lower()
        for soil in SoilType:
            if soil.value == type_of_soil:
                self.__type_of_soil = soil.name
                return
        raise TypeOfSoilError("Некорректный тип почвы")
