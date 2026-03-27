from django.db import models

class FittingModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    image = models.ImageField(upload_to="recreation_area_images", null=True, blank=True, verbose_name="Изображение")

    class Meta:
        db_table = 'Fitting'
        verbose_name = 'Fittings'
        verbose_name_plural = 'Fittings'

    def __str__(self):
        return self.name