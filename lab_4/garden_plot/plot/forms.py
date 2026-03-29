from django import forms
from .models import PlotModel, SoilModel


class PlotForm(forms.ModelForm):
    square = forms.IntegerField()
    perimeter = forms.IntegerField()
    soil = forms.ModelChoiceField(queryset=SoilModel.objects.all())

    class Meta:
        model = PlotModel
        fields = ['square', 'perimeter', 'soil']