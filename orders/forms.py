from django import forms
from .models import Order
from cars.models import Car
import datetime
from django.forms import widgets
from django.contrib.admin import widgets


class InputForm(forms.ModelForm):
    PAYMENT_METHODS = (
        ('1', 'Card'),
        ('2', 'Cash'),
    )
    pick_up_date = forms.DateTimeField(help_text="Enter date and time in format: YYYY-MM-DD")
    drop_off_date = forms.DateTimeField(help_text="Enter date and time in format: YYYY-MM-DD")
    payment_method = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_METHODS)
    car = forms.ModelChoiceField(queryset=Car.objects.all(), label='Car')

    class Meta:
        model = Order
        fields = ('pick_up_date', 'drop_off_date', 'payment_method', 'car')
