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
    pick_up_date = forms.DateTimeField( widget=forms.TextInput(attrs={'id':'pick_up_location','class': 'datetimepicker-input', 'data-toggle':'datetimepicker', 'data-target':'pick_up_location'}))
    drop_off_date = forms.DateTimeField( widget=forms.TextInput(attrs={'id':'pick_up_location','class': 'datetimepicker-input', 'data-toggle':'datetimepicker', 'data-target':'pick_up_location'}))
    payment_method = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_METHODS)
    car = forms.ModelChoiceField(queryset=Car.objects.all(), label='Car')

    class Meta:
        model = Order
        fields = ('pick_up_date', 'drop_off_date', 'payment_method', 'car')
