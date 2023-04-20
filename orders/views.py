from django.shortcuts import render, redirect
from .forms import InputForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.http import HttpResponse
from .models import Order


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@login_required
def order_list(request):
    user = request.user
    orders = Order.objects.filter(client=user.id)
    return render(request, 'orders_list.html', {'orders': orders})

@login_required
def create_order(request):

    form = InputForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            event = form.save(commit=False)
            event.client = request.user
            event.save()
            return redirect('index')
        else:
            messages.error(request, "Error")

    return render(request, 'create_order.html', {'form': form})
