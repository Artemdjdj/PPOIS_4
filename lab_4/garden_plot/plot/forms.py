from django import forms
from django.core.exceptions import ValidationError

from .models import PlotModel, SoilModel
from recreation_area.models import RecreationAreaModel


class BaseForm(forms.ModelForm):
    square = forms.IntegerField()
    perimeter = forms.IntegerField()


class PlotForm(BaseForm):
    soil = forms.ModelChoiceField(queryset=SoilModel.objects.all())

    class Meta:
        model = PlotModel
        fields = ['square', 'perimeter', 'soil']


class RecreationAreaForm(BaseForm):

    def __init__(self, *args, **kwargs):
        self.plot = kwargs.pop('plot', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        if not self.plot:
            raise ValidationError("Ошибка: садовый участок не создан.")

        square = cleaned_data.get('square')
        perimeter = cleaned_data.get('perimeter')

        if square and square > self.plot.square:
            self.add_error('square',
                           f"Площадь зоны ({square}) не может превышать площадь участка ({self.plot.square}).")

        if perimeter and perimeter > self.plot.perimeter:
            self.add_error('perimeter',
                           f"Периметр зоны ({perimeter}) не может превышать периметр участка ({self.plot.perimeter}).")

        return cleaned_data
    class Meta:
        model = RecreationAreaModel
        fields = ['square', 'perimeter']


