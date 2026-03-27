from django.shortcuts import render

from .models import PlantModel


def index(request):
    plants = PlantModel.objects.all()
    context = {'plants':plants}
    return render(request, 'plants/index.html', context)