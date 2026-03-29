from django.db import models

class SoilModel(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    slug = models.SlugField(max_length=50, verbose_name="URL")

    class Meta:
        db_table = 'Soil'
        verbose_name ='Soil'
        verbose_name_plural = 'Soils'

    def __str__(self)->str:
        return self.name


class PlotModel(models.Model):
    square = models.PositiveIntegerField(verbose_name="Площадь")
    perimeter = models.PositiveIntegerField(verbose_name="Периметр")
    soil = models.ForeignKey(SoilModel, on_delete=models.CASCADE, verbose_name="Тип почва")

    class Meta:
        db_table = 'Plot'
        verbose_name ='Plot'
        verbose_name_plural = 'Plots'

    @property
    def soil_name(self):
        return self.soil.soil_name

