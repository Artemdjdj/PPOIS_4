from typing import Dict, Any
from src.exceptions.exceptions import (
    BigAmountOfFertilizerError,
)
from src.main.settings import MAX_COEFF, NORMAL_COEFF
from src.utils.validator import SoilValidator, SoilType


class Soil:
    def __init__(self, soil_type: SoilType = SoilType.LOAMY):
        self.__validator = None
        self.__type_of_soil: str = soil_type.value
        self.__coeff_fertilizer: int | float = NORMAL_COEFF

    @property
    def type_of_soil(self) -> str:
        return self.__type_of_soil

    @type_of_soil.setter
    def type_of_soil(self, type_of_soil: str) -> None:
        type_of_soil = type_of_soil.lower()
        self.__validator = SoilValidator(type_of_soil)
        self.__validator.validate()
        self.__type_of_soil = type_of_soil

    def fertilize(self, coeff_fertilizer: int | float) -> None:
        if self.__coeff_fertilizer + coeff_fertilizer <= MAX_COEFF:
            self.__coeff_fertilizer += coeff_fertilizer
        raise BigAmountOfFertilizerError(
            "Слишком много удобрений, почва будет перенасыщена, уменьшите количество!"
        )

    def create_dict(self) -> Dict[str, Any]:
        return {"soil_type": self.type_of_soil}

    @classmethod
    def create_object_from_dict(cls, info_dict: Dict[str, Any]) -> 'Soil':
        return cls(soil_type=SoilType(info_dict["soil_type"]))
