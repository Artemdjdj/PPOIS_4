from enum import Enum
from src.exceptions.exceptions import (
    TypeOfSoilError,
    BigAmountOfFertilizerError,
)
from src.main.settings import MAX_COEFF, NORMAL_COEFF


class SoilType(Enum):
    CLAY = "глинистая"
    SANDY = "песчаная"
    LOAMY = "суглинистая"
    PEATY = "торфяная"
    CHALKY = "известковая"
    CHERNOZEM = "чернозём"


class Soil:
    def __init__(self, soil_type: SoilType = SoilType.LOAMY):
        self.__type_of_soil: SoilType = soil_type
        self.__coeff_fertilizer: int | float = NORMAL_COEFF

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
    
    def fertilize(self, coeff_fertilizer: int | float) -> None:
        if self.__coeff_fertilizer + coeff_fertilizer <= MAX_COEFF:
            self.__coeff_fertilizer += coeff_fertilizer
        raise BigAmountOfFertilizerError(
            "Слишком много удобрений, почва будет перенасыщена, уменьшите количество!"
        )
