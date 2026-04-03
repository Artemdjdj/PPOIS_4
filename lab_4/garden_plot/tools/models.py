from django.db import models
from django.utils import timezone

from plot.models import PlotModel

from garden_plot.exceptions import BrokenToolError
from garden_plot.settings import COUNT_OF_WORK_HOURS_WORN, COUNT_OF_WORK_HOURS_BROKEN


class ToolTypeModel(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True, verbose_name="URL")

    class Meta:
        db_table = "ToolType"
        verbose_name = "ToolType"
        verbose_name_plural = "ToolTypes"

    def __str__(self):
        return self.name


class ToolStateModel(models.Model):
    name = models.CharField(max_length=20, verbose_name="Название")
    slug = models.SlugField(max_length=20, unique=True, blank=True, null=True, verbose_name="URL")

    class Meta:
        db_table = "ToolState"
        verbose_name = "ToolState"
        verbose_name_plural = "ToolStates"

    def __str__(self) -> str:
        return self.name


class ToolModel(models.Model):
    tool_type = models.ForeignKey(ToolTypeModel, on_delete=models.CASCADE, verbose_name="Тип")
    brand = models.CharField(max_length=65, verbose_name="Бренд")
    description = models.CharField(max_length=50, verbose_name="Комментарии")
    state = models.ForeignKey(ToolStateModel, on_delete=models.CASCADE, verbose_name="Cостояние")
    usage_count = models.PositiveIntegerField(default=0, verbose_name="Часов использования")
    date_of_maintain = models.DateField(auto_now_add=True, verbose_name="Дата обслуживания")
    image = models.ImageField(upload_to="tool_images", null=True, blank=True, verbose_name="Изображение")
    plot = models.ForeignKey(
        PlotModel,
        on_delete=models.CASCADE,
        related_name='tools',
        verbose_name="Садовый участок"
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

    def default_maintain(self):
        self.state = ToolStateModel.objects.get(name="хорошее")
        self.usage_count: int | float = 0
        self.date_of_maintain = timezone.now()

    def maintenance(self):
        if self.state.name == "идеальное":
            return "Инструмент новый, обслуживание не надо"
        elif self.state.name == "хорошее":
            return "Инструмент в хорошем состоянии, можно приступать к работе"
        elif self.state.name == "поврежденное":
            self.default_maintain()
            return "Инструмент имел небольшие дефекты, теперь все готово, инструмент в хорошем состоянии"
        else:
            self.default_maintain()
            return "Инструмент был сильно поврежден, теперь все готово, инструмент в хорошем состоянии"

    def perform_task(self, work_hours: int | float) -> None:
        if self.state.name == "сломанное":
            raise BrokenToolError("Инструмент сломан")
        self.usage_count += work_hours
        if (
                COUNT_OF_WORK_HOURS_WORN <= self.usage_count <= COUNT_OF_WORK_HOURS_BROKEN
        ):
            self.state = ToolStateModel.objects.get(name="поврежденное")
        elif self.usage_count > COUNT_OF_WORK_HOURS_BROKEN:
            self.state = ToolStateModel.objects.get(name="сломанное")
