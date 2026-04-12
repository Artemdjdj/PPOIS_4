from django import forms
from .models import ToolStateModel, ToolTypeModel, ToolModel


class ToolForm(forms.ModelForm):
    tool_type = forms.ModelChoiceField(queryset=ToolTypeModel.objects.all())
    brand = forms.CharField()
    description = forms.CharField()
    image = forms.ImageField()

    class Meta:
        model = ToolModel
        fields = [
            "tool_type",
            "brand",
            "description",
            "image",
        ]
