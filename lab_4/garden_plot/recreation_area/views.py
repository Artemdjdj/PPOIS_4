from django.shortcuts import render
from .models import FittingModel, GrillModel, MeatTypeModel


def index(request):
    fittings = FittingModel.objects.all()
    return render(request, 'recreation_area/index.html', context={'fittings': fittings})

def grill(request):
    grill = GrillModel.objects.get_obj()
    meat_types =MeatTypeModel.objects.all()
    meat_type_last = None
    result_time_of_frying = None
    if request.method == 'POST':
        meat_id = request.POST.get('meat_type')
        meat_type_last = MeatTypeModel.objects.get(id=meat_id)
        result_time_of_frying = meat_id

    context = {
        'grill': grill,
        'meat_types': meat_types,
        'result_time_of_frying': result_time_of_frying,
        'meat_type_last': meat_type_last,
    }
    return render(request, 'recreation_area/grill.html', context)