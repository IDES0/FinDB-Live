from django.shortcuts import render
from .models import ModelDescription

def model_list(request):
    models = ModelDescription.objects.all()
    return render(request, 'models/model_list.html', {'models': models})