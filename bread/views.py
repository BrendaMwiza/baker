from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Categories,Bakery,Order
from .forms import OrderForm,BakeryForm

def page(request):
    current_user = request.user
    return render(request,'all-pages/index.html',{})

    images=Bakery.objects.all()
    return render(request,'all-pages/index.html',{"images":images})

def bread(request):
    return render(request,'all-pages/bread.html',{})

def cookies(request):
    return render(request,'all-pages/cookies.html',{})

def cakes(request):
    return render(request,'all-pages/cakes.html',{})

def snacks(request):
    return render(request,'all-pages/snacks.html',{}) 

def about(request):
    return render(request,'all-pages/about.html',{})             

def contact(request):
    return render(request,'all-pages/contact.html',{}) 

    
@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = BakeryForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('page')

    else:
        form = BakeryForm()
    return render(request, 'all-pages/post.html', {"form": form})


def order(request):
    current_user = request.user
    order=Order.objects.all()
    return render(request, 'all-pages/order.html', {"order":order})
  

def order_form(request):
   current_user = request.user
   order=Order.objects.all()
   if request.method == 'POST':
       form = OrderForm(request.POST, request.FILES)
       if form.is_valid():
           order = form.save(commit=False)
           order.user = current_user
           order.save()
       return redirect('orderform')
   else:
       form = OrderForm()
   return render(request, 'all-pages/orderform.html', {"form": form,"order":order})    





