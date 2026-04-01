from django.db import models

from plot.models import PlotModel


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

    def __str__(self)->str:
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


