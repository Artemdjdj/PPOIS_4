from django import forms
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
    class Meta:
        model = RecreationAreaModel
        fields = ['square', 'perimeter']
