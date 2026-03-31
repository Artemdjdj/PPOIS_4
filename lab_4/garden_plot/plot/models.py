from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator,  MaxValueValidator
from recreation_area.utils import BaseManager

class SoilModel(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    slug = models.SlugField(max_length=50, verbose_name="URL")

    class Meta:
        db_table = 'Soil'
        verbose_name = 'Soil'
        verbose_name_plural = 'Soils'

    def __str__(self) -> str:
        return self.name


class PlotManager(BaseManager):
    def get_obj(self):
        try:
            return self.get()
        except PlotModel.DoesNotExist:
            return None

class PlotModel(models.Model):
    square = models.PositiveIntegerField(validators=[MinValueValidator(100), MaxValueValidator(10000)], verbose_name="Площадь")
    perimeter = models.PositiveIntegerField(validators=[MinValueValidator(100), MaxValueValidator(10000)], verbose_name="Периметр")
    soil = models.ForeignKey(SoilModel, on_delete=models.CASCADE, verbose_name="Тип почвы")

    objects = PlotManager()

    class Meta:
        db_table = 'Plot'
        verbose_name = 'Plot'
        verbose_name_plural = 'Plots'

    def save(self, *args, **kwargs):
        if not self.pk and PlotModel.objects.exists():
            raise ValidationError("Может существовать только один участок.")
        super().save(*args, **kwargs)

    @property
    def soil_name(self):
        return self.soil.name

    def __str__(self):
        return f"Участок №{self.pk}"

    def get_tools(self):
        return self.tools.all()

    def get_plants(self):
        return self.plants.all()
