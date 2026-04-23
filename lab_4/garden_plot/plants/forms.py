from django import forms
from .models import ColorModel, PlantModel


class PlantForm(forms.ModelForm):
    height = forms.IntegerField()
    name = forms.CharField()
    color = forms.ModelChoiceField(queryset=ColorModel.objects.all())
    diameter = forms.IntegerField()
    image = forms.ImageField(required=False)

    class Meta:
        model = PlantModel
        fields = [
            "height",
            "name",
            "color",
            "diameter",
            "image",
        ]
