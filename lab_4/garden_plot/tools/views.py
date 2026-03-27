from django.shortcuts import render

from .models import ToolModel


def index(request):
    tools = ToolModel.objects.all()
    context = {'tools': tools}
    return render(request, "tools/index.html", context)