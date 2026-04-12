from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from recreation_area.utils import BaseManager
from garden_plot.exceptions import BigAmountOfFertilizerError

from garden_plot.settings import MAX_COEFF, NORMAL_COEFF
from src.core.soil import Soil, SoilType

class SoilModel(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=50, unique=True, verbose_name="URL")
    coeff_fertilizer = models.DecimalField(default=NORMAL_COEFF, max_digits=4, decimal_places=2,
                                           verbose_name="Коэффициент засоленности")

    class Meta:
        db_table = 'Soil'
        verbose_name = 'Soil'
        verbose_name_plural = 'Soils'

    def __str__(self) -> str:
        return self.name

    # def fertilize(self, coeff_fertilize):
    #     if self.coeff_fertilizer + coeff_fertilize <= MAX_COEFF:
    #         self.coeff_fertilizer += coeff_fertilize
    #         self.save()
    #     else:
    #         raise BigAmountOfFertilizerError(
    #             "Слишком много удобрений, почва будет перенасыщена, уменьшите количество!"
    #         )

    def clear_soil(self):
        self.coeff_fertilizer = NORMAL_COEFF
        self.save()

    def to_library_soil(self) -> Soil:
        soil_type = SoilType(self.name.lower())
        convert_soil = Soil(soil_type=soil_type)
        convert_soil.coeff_fertilizer = self.coeff_fertilizer
        return convert_soil

    @classmethod
    def from_library_soil(cls, convert_soil: Soil) -> "SoilModel":
        return cls(
            name=convert_soil.type_of_soil.capitalize(),
            slug=convert_soil.type_of_soil,
            coeff_fertilizer=convert_soil.coeff_fertilizer,
        )

    def update_from_library_soil(self, convert_soil: Soil) -> None:
        self.name = convert_soil.type_of_soil.capitalize()
        self.slug = convert_soil.type_of_soil
        self.coeff_fertilizer = convert_soil.coeff_fertilizer
        self.save()


class PlotManager(BaseManager):
    def get_obj(self):
        try:
            return self.get()
        except PlotModel.DoesNotExist:
            return None


class PlotModel(models.Model):
    square = models.PositiveIntegerField(validators=[MinValueValidator(100), MaxValueValidator(10000)],
                                         verbose_name="Площадь")
    perimeter = models.PositiveIntegerField(validators=[MinValueValidator(100), MaxValueValidator(10000)],
                                            verbose_name="Периметр")
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
