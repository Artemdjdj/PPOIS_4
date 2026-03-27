from django.shortcuts import render
from .models import FittingModel

def index(request):
    fittings = FittingModel.objects.all()
    return render(request, 'recreation_area/index.html', context={'fittings': fittings})