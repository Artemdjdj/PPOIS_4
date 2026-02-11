from enum import Enum
from src.utils.descriptor import NumberValidator
from src.utils.descriptor import IntegerValidator

class SoilType(Enum):
    CLAY = "глинистая"
    SANDY = "песчаная"
    LOAMY = "суглинистая"
    PEATY = "торфяная"
    CHALKY = "известковая"
    CHERNOZEM = "чернозём"

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
        self.square = square
        self.perimeter = perimeter


class Alcove(BasicObject):
    human_count = IntegerValidator()

    def __init__(
        self, square: int | float, perimeter: int | float, human_count: int
    ) -> None:
        super().__init__(square, perimeter)
        self.human_count = human_count


class Grill:
    def fry(self, meat:MeatType)->str:
        return f"мясо приготовилось за {meat.cooking_time} минут"