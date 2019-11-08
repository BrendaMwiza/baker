from django import forms
from .models import Bakery,Order

class BakeryForm(forms.ModelForm):
    class Meta:
        model = Bakery
        exclude = [] 

class  OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['post']      