from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from .models import Car


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})
