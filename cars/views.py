from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Car


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})