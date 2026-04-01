from django import forms
from .models import ColorModel, PlantModel


class PlantForm(forms.ModelForm):
    height = forms.IntegerField()
    name = forms.CharField()
    color = forms.MultipleChoiceField(queryset=ColorModel.objects.all())
    diameter = forms.IntegerField()
    is_watered = forms.BooleanField()
    time_of_last_adding_water = forms.IntegerField()
    image = forms.ImageField()

    class Meta:
        model = PlantModel
        fields = [
            'height',
            'name',
            'color',
            'diameter',
            'is_watered',
            'time_of_last_adding_water',
            'image',
            'plot'
        ]