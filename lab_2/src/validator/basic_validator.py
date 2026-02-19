from abc import ABC, abstractmethod


class BasicValidator(ABC):
    @abstractmethod
    def validate(self) -> None:
        pass


class BasicDateValidator(BasicValidator):
    @abstractmethod
    def validate(self) -> None:
        pass


class BasicAddressValidator(BasicValidator):
    @abstractmethod
    def validate(self) -> None:
        pass
