from django.shortcuts import render

def index(request):
    return render(request, 'recreation_area/index.html')