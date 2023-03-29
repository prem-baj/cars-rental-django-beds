from django.shortcuts import render, redirect
from .forms import InputForm
from django.contrib import messages

# Create your views here.

from django.http import HttpResponse
from .models import Order


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders_list.html', {'orders': orders})


def create_order(request):

    form = InputForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            event = form.save(commit=False)
            #event.customer = request.user
            event.save()
            return redirect('index')
        else:
            messages.error(request, "Error")

    return render(request, 'create_order.html', {'form': form})
