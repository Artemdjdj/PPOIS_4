from django import forms
from .models import ToolStateModel, ToolTypeModel, ToolModel


class ToolForm(forms.ModelForm):
    tool_type = forms.MultipleChoiceField(queryset=ToolTypeModel.objects.all())
    brand = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    state = forms.MultipleChoiceField(queryset=ToolStateModel.objects.all())
    usage_count = forms.IntegerField()
    date_of_maintain = forms.DateField()
    image = forms.ImageField()

    class Meta:
        model = ToolModel
        fields = [
            'tool_type',
            'brand',
            'description',
            'state',
            'usage_count',
            'date_of_maintain',
            'image',
            'plot'
        ]
