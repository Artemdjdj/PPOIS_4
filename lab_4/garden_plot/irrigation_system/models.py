from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from plot.models import PlotModel
from recreation_area.utils import BaseManager


class IrrigationSystemManager(BaseManager):
    def get_obj(self):
        try:
            return self.get()
        except IrrigationSystemModel.DoesNotExist:
            return None

class IrrigationSystemModel(models.Model):
    is_active = models.BooleanField(default=False, verbose_name='Включена ли')
    time_of_last_adding_water = models.PositiveIntegerField(default=10, verbose_name="Время с поледнего полива в секундах")
    plot = models.OneToOneField(
        PlotModel,
        on_delete=models.CASCADE,
        verbose_name="Участок"
    )
    objects = IrrigationSystemManager()

    def save(self, *args, **kwargs):
        if not self.pk and IrrigationSystemModel.objects.exists():
            raise ValidationError("Может существовать только одна система полива.")
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'IrrigationSystem'
        verbose_name = 'IrrigationSystem'
        verbose_name_plural = 'IrrigationSystems'