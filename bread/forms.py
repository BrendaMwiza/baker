from django import forms
from .models import Post,Order

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['code'] 

class  OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['']      