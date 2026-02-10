from src.utils.descriptor import NumberValidator


class Soil:
    coeff_water = NumberValidator(1)
    coeff_fertilizer = NumberValidator(1)

    def __init__(
        self, type_of_soil: str, coeff_water: int | float, coeff_fertilizer: int | float
    ):
        self.__type_of_soil = type_of_soil
        self.coeff_water = coeff_water
        self.coeff_fertilizer = coeff_fertilizer
    
    @property
    def type_of_soil(self)->str:
        return self.__type_of_soil
    
    @type_of_soil.setter
    def type_of_soil(self, type_of_soil:str)->None:
        if not isinstance(type_of_soil, str):
            raise ValueError("Тип почвы должен быть строкой")
        self.__type_of_soil = type_of_soil