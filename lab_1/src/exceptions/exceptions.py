class TypeOfSoilError(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self.msg: str = msg


class GrillDoesNotExist(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self.msg: str = msg


class BigAmountOfFertilizerError(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self.msg: str = msg


class SystemIsNotActiveError(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self.msg: str = msg


class LackOfWaterError(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self.msg: str = msg


class TooMuchPlantsAreWateredError(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self.msg: str = msg


class PositionError(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self.msg: str = msg


class SizeError(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self.msg: str = msg

class NoneObjectError(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self.msg: str = msg
