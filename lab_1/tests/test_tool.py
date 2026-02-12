import pytest
from datetime import date
from src.core.tool import Tool
from src.exceptions.exceptions import BrokenToolError

class TestTool:
    def test_tool_creation(self):
        tool = Tool("Пила", "STIHL", "Бензопила")
        assert tool.name == "Пила"
        assert tool.brand == "STIHL"
        assert tool.description == "Бензопила"
        assert tool.state == "идеальное"
        assert tool.usage_count == 0
        assert tool.date_of_maintain == date.today()

    def test_perform_task(self):
        tool = Tool("Молоток", "Something", "Строительный молоток")
        tool.perform_task(5)
        assert tool.usage_count == 5
        assert tool.state == "идеальное"
        tool.perform_task(15)
        assert tool.state == "поврежденное"
        tool.perform_task(6)
        assert tool.state == "сломанное"
        with pytest.raises(BrokenToolError):
            tool.perform_task(6)

    def test_maintenance(self):
        tool = Tool("Шуруповерт", "Makita", "Мощный")
        assert tool.maintenance() == "Инструмент новый, обслуживание не надо"
        tool.perform_task(13)
        assert tool.state == "поврежденное"
        assert (
            "Инструмент имел небольшие дефекты, теперь все готово инструмент и хорошем состоянии"
            == tool.maintenance()
        )
        assert tool.state == "хорошее"
        assert tool.usage_count == 0
        

    def test_str_method(self):
        tool = Tool("Лопата", "Fiskars", "Штыковая лопата")
        assert str(tool) == "Инструмент: Лопата, бренд: Fiskars"
