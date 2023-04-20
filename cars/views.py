from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
from django.contrib.auth.decorators import login_required


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@login_required
def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})
