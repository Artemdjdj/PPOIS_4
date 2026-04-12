from decimal import Decimal

from django.db import models
from django.utils import timezone

from plot.models import PlotModel

from garden_plot.exceptions import BrokenToolError
from garden_plot.settings import COUNT_OF_WORK_HOURS_WORN, COUNT_OF_WORK_HOURS_BROKEN
from src.core.tool import Tool, ToolState


class ToolTypeModel(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=50, unique=True, blank=True, null=True, verbose_name="URL"
    )

    class Meta:
        db_table = "ToolType"
        verbose_name = "ToolType"
        verbose_name_plural = "ToolTypes"

    def __str__(self):
        return self.name


class ToolStateModel(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=20, unique=True, blank=True, null=True, verbose_name="URL"
    )

    class Meta:
        db_table = "ToolState"
        verbose_name = "ToolState"
        verbose_name_plural = "ToolStates"

    def __str__(self) -> str:
        return self.name


class ToolModel(models.Model):
    tool_type = models.ForeignKey(
        ToolTypeModel, on_delete=models.CASCADE, verbose_name="Тип"
    )
    brand = models.CharField(max_length=65, verbose_name="Бренд")
    description = models.CharField(max_length=50, verbose_name="Комментарии")
    state = models.ForeignKey(
        ToolStateModel, on_delete=models.CASCADE, verbose_name="Cостояние"
    )
    usage_count = models.DecimalField(
        default=0.0, max_digits=5, decimal_places=2, verbose_name="Часов использования"
    )
    date_of_maintain = models.DateField(
        auto_now_add=True, verbose_name="Дата обслуживания"
    )
    image = models.ImageField(
        upload_to="tool_images", null=True, blank=True, verbose_name="Изображение"
    )
    plot = models.ForeignKey(
        PlotModel,
        on_delete=models.CASCADE,
        related_name="tools",
        verbose_name="Садовый участок",
    )

    class Meta:
        db_table = "Tool"
        verbose_name = "Tool"
        verbose_name_plural = "Tools"

    @property
    def tool_type_name(self):
        return self.tool_type.name

    @property
    def state_name(self):
        return self.state.name

    #     def default_maintain(self):
    #         self.state = ToolStateModel.objects.get(name="хорошее")
    #         self.usage_count: int | float = 0
    #         self.date_of_maintain = timezone.now()
    #         self.save()
    #
    #     def maintenance(self):
    #         if self.state.name == "идеальное":
    #             return "Инструмент новый, обслуживание не надо"
    #         elif self.state.name == "хорошее":
    #             return "Инструмент в хорошем состоянии, можно приступать к работе"
    #         elif self.state.name == "поврежденное":
    #             self.default_maintain()
    #             return "Инструмент имел небольшие дефекты, теперь все готово, инструмент в хорошем состоянии"
    #         else:
    #             self.default_maintain()
    #             return "Инструмент был сильно поврежден, теперь все готово, инструмент в хорошем состоянии"
    #
    #     def perform_task(self, work_hours: int | float) -> None:
    #         if self.state.name == "сломанное":
    #             raise BrokenToolError("Инструмент сломан")
    #         self.usage_count += Decimal(str(work_hours))
    #         if COUNT_OF_WORK_HOURS_WORN <= self.usage_count <= COUNT_OF_WORK_HOURS_BROKEN:
    #             self.state = ToolStateModel.objects.get(name="поврежденное")
    #         elif self.usage_count > COUNT_OF_WORK_HOURS_BROKEN:
    #             self.state = ToolStateModel.objects.get(name="сломанное")
    #
    #         self.save()

    def to_library_tool(self) -> Tool:
        data = {
            "name": self.tool_type.name,
            "brand": self.brand,
            "description": self.description,
            "state": self.state.name,
            "usage_count": float(self.usage_count),
            "date_of_maintain": self.date_of_maintain.isoformat(),
        }

        return Tool.create_object_from_dict(data)

    @classmethod
    def from_library_tool(
        cls,
        tool: Tool,
        plot: PlotModel,
        image=None,
    ) -> "ToolModel":
        tool_type, _ = ToolTypeModel.objects.get_or_create(name=tool.name)

        state = ToolStateModel.objects.get(name=tool.state)

        return cls(
            tool_type=tool_type,
            brand=tool.brand,
            description=tool.description,
            state=state,
            usage_count=Decimal(str(tool.usage_count)),
            date_of_maintain=tool.date_of_maintain,
            plot=plot,
            image=image,
        )

    def update_from_library_tool(self, tool: Tool) -> None:

        tool_type, _ = ToolTypeModel.objects.get_or_create(name=tool.name)
        self.tool_type = tool_type

        self.brand = tool.brand
        self.description = tool.description
        self.state = ToolStateModel.objects.get(name=tool.state)
        self.usage_count = Decimal(str(tool.usage_count))
        self.date_of_maintain = tool.date_of_maintain

        self.save()
