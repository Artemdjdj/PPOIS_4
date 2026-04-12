from abc import ABC, abstractmethod

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from plot.models import PlotModel
from recreation_area.utils import BaseManager
from src.core.plot import Grill


class MeatTypeModel(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")
    slug = models.SlugField(max_length=30, verbose_name="URL")
    time_of_cooking = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(300)],
                                         verbose_name="Среднее время приготовления мин")
    image = models.ImageField(upload_to='meat_images', null=True, blank=True, verbose_name="Изображение")

    class Meta:
        db_table = 'MeatType'
        verbose_name = 'MeatType'
        verbose_name_plural = 'MeatTypes'

    def __str__(self):
        return self.name

class RecreationAreaManager(BaseManager):
    def get_obj(self):
        try:
            return self.get()
        except RecreationAreaModel.DoesNotExist:
            return None

class RecreationAreaModel(models.Model):
    square = models.PositiveIntegerField(validators=[MinValueValidator(100), MaxValueValidator(10000)], verbose_name="Площадь")
    perimeter = models.PositiveIntegerField(validators=[MinValueValidator(100), MaxValueValidator(10000)], verbose_name="Периметр")
    is_clean = models.BooleanField(default=False, verbose_name="Убрана")
    plot = models.OneToOneField(PlotModel, on_delete=models.CASCADE, verbose_name="Участок")
    objects = RecreationAreaManager()

    def save(self, *args, **kwargs):
        if not self.pk and RecreationAreaModel.objects.exists():
            raise ValidationError("Может существовать только одна зона отдыха.")
        super().save(*args, **kwargs)

    def get_fittings(self):
        return self.fittings.all()

#     def to_library_area(self) -> RecreationArea:
#         convert_area = RecreationArea(square=self.square, perimeter=self.perimeter)
#         for fitting_model in self.fittings.all():
#             convert_area.add_decorative_fitting(fitting_model.name)
#         if GrillModel.objects.filter(recreation_area=self).exists():
#             convert_area.put_grill()
#         if self.is_clean:
#             convert_area.clean()
#         return convert_area
# 
#     @classmethod
#     def from_library_area(cls, lib_area: RecreationArea, plot: PlotModel) -> "RecreationAreaModel":
#         area_model = cls(square=lib_area.square, perimeter=lib_area.perimeter, plot=plot, is_clean=lib_area.is_clean)
#         area_model.save()
#         for fitting in lib_area.get_decorative_fittings():
#             FittingModel.objects.create(name=fitting.name, recreation_area=area_model)
#         if lib_area._RecreationArea__grill is not None:
#             GrillModel.objects.create(recreation_area=area_model)
#         return area_model
# 
#     def update_from_library_area(self, lib_area: RecreationArea) -> None:
#         self.square = lib_area.square
#         self.perimeter = lib_area.perimeter
#         self.is_clean = lib_area.is_clean
#         self.save()
#         current_fittings = set(self.fittings.values_list('name', flat=True))
#         lib_fittings = set(f.name for f in lib_area.get_decorative_fittings())
#         for name in lib_fittings - current_fittings:
#             FittingModel.objects.create(name=name, recreation_area=self)
#         for name in current_fittings - lib_fittings:
#             self.fittings.filter(name=name).delete()
#         has_grill = GrillModel.objects.filter(recreation_area=self).exists()
#         lib_has_grill = lib_area._RecreationArea__grill is not None
#         if lib_has_grill and not has_grill:
#             GrillModel.objects.create(recreation_area=self)
#         elif not lib_has_grill and has_grill:
#             GrillModel.objects.filter(recreation_area=self).delete()

    class Meta:
        db_table = 'RecreationArea'
        verbose_name = 'RecreationArea'
        verbose_name_plural = 'RecreationAreas'

    def __str__(self):
        return f"Зона отдыха №{self.pk}"


class FittingModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    image = models.ImageField(upload_to="recreation_area_images", null=True, blank=True, verbose_name="Изображение")
    recreation_area = models.ForeignKey(
        RecreationAreaModel,
        on_delete=models.CASCADE,
        related_name='fittings',
        verbose_name="Зона отдыха"
    )
    class Meta:
        db_table = 'Fitting'
        verbose_name = 'Fitting'
        verbose_name_plural = 'Fittings'

    def __str__(self):
        return self.name

class GrillManager(BaseManager):
    def get_obj(self):
        try:
            return self.get()
        except GrillModel.DoesNotExist:
            return None

class GrillModel(models.Model):
    recreation_area = models.ForeignKey(
        RecreationAreaModel,
        on_delete=models.CASCADE,
        verbose_name="Зона отдыха"
    )
    objects = GrillManager()

    def save(self, *args, **kwargs):
        if not self.pk and GrillModel.objects.exists():
            raise ValidationError("Может существовать только один гриль.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Гриль {self.pk} для приготовления мясных блюд"

    def to_library_grill(self) -> Grill:
        return Grill()

    @classmethod
    def from_library_grill(cls, lib_grill: Grill, recreation_area: RecreationAreaModel) -> "GrillModel":
        return cls(recreation_area=recreation_area)

    def update_from_library_grill(self, lib_grill: Grill) -> None:
        self.save()

    class Meta:
        db_table = 'Grill'
        verbose_name = 'Grill'
        verbose_name_plural = 'Grills'





