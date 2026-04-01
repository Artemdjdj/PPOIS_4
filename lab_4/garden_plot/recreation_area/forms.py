from django import forms
from django.core.exceptions import ValidationError

from recreation_area.models import RecreationAreaModel

from recreation_area.models import FittingModel


class FittingForm(forms.ModelForm):
    name = forms.CharField()
    image = forms.ImageField()

    class Meta:
        model = FittingModel
        fields = ['name', 'image']




