import pytest
from src.core.irrigation_system import IrrigationSystem
from src.core.plant import Color, Plant
from src.exceptions.exceptions import (
    SystemIsNotActiveError,
    LackOfWaterError,
    TooMuchPlantsAreWateredError,
)


class TestIrrigationSystem:
    def test_amount_of_water(self):
        system = IrrigationSystem(123)
        assert system.amount_of_all_water == 123
        with pytest.raises(SystemIsNotActiveError):
            system.water(10, [])

    def test_turn_on_off(self):
        system = IrrigationSystem(100)
        system.turn_on()
        plants = []
        system.water(10, plants)
        assert system.amount_of_all_water == 90
        system.turn_of()
        with pytest.raises(SystemIsNotActiveError):
            system.water(10, plants)

    def test_water_success(self):
        system = IrrigationSystem(54)
        system.turn_on()
        plant1 = Plant(10, "Роза", Color(), diameter=50)
        plant2 = Plant(10, "Тюльпан", Color(), diameter=30)
        plants = [plant1, plant2]
        assert not plant1.is_watered
        assert not plant2.is_watered
        system.water(20, plants)
        assert plant1.is_watered is True
        assert plant2.is_watered is True
        assert system.amount_of_all_water == 34

    def test_water_lack_of_water(self):
        system = IrrigationSystem(10)
        system.turn_on()
        with pytest.raises(LackOfWaterError):
            system.water(20, [])

    def test_too_much_water(self):
        system = IrrigationSystem(100)
        system.turn_on()
        plant1 = Plant(10, "A", Color(), is_watered=True, diameter=1)
        plant2 = Plant(10, "B", Color(), is_watered=False, diameter=1)
        plant3 = Plant(10, "C", Color(), is_watered=True, diameter=1)
        plants = [plant1, plant2, plant3]
        with pytest.raises(TooMuchPlantsAreWateredError):
            system.water(10, plants)

    def test_amount_of_water_validation(self):
        with pytest.raises(ValueError):
            IrrigationSystem(-10)
