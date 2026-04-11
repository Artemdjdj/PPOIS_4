import pytest
from datetime import datetime, timezone, timedelta
from src.core.irrigation_system import IrrigationSystem
from src.core.plant import Color, Plant
from src.exceptions.exceptions import (
    SystemIsNotActiveError,
    TooMuchPlantsAreWateredError,
)

MIN_TIME_OF_WATERING = 10

class TestIrrigationSystem:
    def test_amount_of_water(self):
        system = IrrigationSystem()
        with pytest.raises(SystemIsNotActiveError):
            system.water([])

    def test_turn_on_off(self):
        system = IrrigationSystem()
        system.turn_on()
        plant = Plant(10, "Тест", Color(), diameter=1)
        plants = [plant]
        result = system.water(plants)
        assert result == "Не политые растения были успешно политы, вскоре вы нужно будет их снова полить"
        assert plant.is_watered is True
        system.turn_of()
        with pytest.raises(SystemIsNotActiveError):
            system.water(plants)

    def test_water_success(self):
        system = IrrigationSystem()
        system.turn_on()
        plant1 = Plant(10, "Роза", Color(), diameter=50)
        plant2 = Plant(10, "Тюльпан", Color(), diameter=30)
        plants = [plant1, plant2]
        assert not plant1.is_watered
        assert not plant2.is_watered
        result = system.water(plants)
        assert result == "Не политые растения были успешно политы, вскоре вы нужно будет их снова полить"
        assert plant1.is_watered is True
        assert plant2.is_watered is True
        assert system.is_active is False

    def test_too_much_water(self):
        system = IrrigationSystem()
        system.turn_on()
        plant1 = Plant(10, "A", Color(), is_watered=True, diameter=1)
        plant2 = Plant(10, "B", Color(), is_watered=False, diameter=1)
        plant3 = Plant(10, "C", Color(), is_watered=True, diameter=1)
        plants = [plant1, plant2, plant3]
        system.time_of_last_adding_water = datetime.now(timezone.utc).replace(tzinfo=None)
        with pytest.raises(TooMuchPlantsAreWateredError):
            system.water(plants)

    def test_water_empty_plants(self):
        system = IrrigationSystem()
        system.turn_on()
        with pytest.raises(ValueError, match="У вас нет растений"):
            system.water([])

    def test_water_after_cooldown(self):
        system = IrrigationSystem()
        system.turn_on()
        plant = Plant(10, "Ромашка", Color(), diameter=5)
        plants = [plant]
        result1 = system.water(plants)
        assert result1 == "Не политые растения были успешно политы, вскоре вы нужно будет их снова полить"
        assert plant.is_watered is True
        system.turn_on()
        with pytest.raises(TooMuchPlantsAreWateredError):
            system.water(plants)
        past_time = datetime.now(timezone.utc).replace(tzinfo=None) - timedelta(seconds=MIN_TIME_OF_WATERING + 1)
        system.time_of_last_adding_water = past_time
        system.turn_on()
        result2 = system.water(plants)
        assert result2 == "Не политые растения были успешно политы, вскоре вы нужно будет их снова полить"