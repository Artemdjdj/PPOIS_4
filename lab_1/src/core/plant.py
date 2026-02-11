from abc import ABC, abstractmethod
from src.utils.descriptor import NumberValidator
from src.utils.utils import Color
from src.main.settings import MAX_DIAMETER_OF_PLANT


class IPlant(ABC):
    height = NumberValidator()
    diameter = NumberValidator(MAX_DIAMETER_OF_PLANT)

    def __init__(
        self,
        height: int | float,
        name: str,
        color: Color,
        is_watered:bool=False,
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
        return self.__color.name
    
    @property
    def is_watered(self) -> bool:
        return self.__is_watered

    @is_watered.setter
    def is_watered(self, is_watered) -> None:
        self.__is_watered = is_watered

    @abstractmethod
    def is_edible(self) -> bool:
        pass


class Vegetable(IPlant):
    length_root = NumberValidator()

    def __init__(
        self,
        height: int | float,
        name: str,
        color: Color,
        length_root: int | float,
        is_watered:bool = False
    ):
        super.__init__(height, name, color, is_watered)
        self.length_root = length_root

    def get_type_of_plant(self):
        return "Vegetable"

    def is_edible(self) -> bool:
        return True


class Fruit(IPlant):
    def __init__(
        self,
        height: int | float,
        name: str,
        color: Color,
        is_sweet: bool,
        is_watered:bool = False
    ):
        super.__init__(height, name, color, is_watered)
        self.__is_sweet = is_sweet

    @property
    def is_sweet(self) -> bool:
        return self.__is_sweet

    @is_sweet.setter
    def is_sweet(self, is_sweet: bool) -> None:
        self.__is_sweet = is_sweet

    def is_edible(self) -> bool:
        return True


class DecorativePlant(IPlant):
    def __init__(
        self,
        height: int | float,
        name: str,
        color: Color,
        design: str,
        is_watered:bool = False
    ):
        super.__init__(height, name, color, is_watered)
        self.__design = design

    @property
    def design(self) -> str:
        return self.__design

    @design.setter
    def design(self, design: str) -> None:
        self.__design = design

    def is_edible(self) -> bool:
        return False
