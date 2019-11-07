from django.shortcuts import render,redirect
from .models import Bakery,Order,Categories
# from django.contrib.auth.decorators import login_required
from .forms import BakeryForm,OrderForm

def index(request):
    images=Bakery.objects.all()
    return render(request,'my_bread/index.html',{"images":images})

def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = BakeryForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('home')

    else:
        form = BakeryForm()
    return render(request, 'my_bread/post.html', {"form": form})


# @login_required(login_url='/accounts/login/')
def order(request):
    current_user = request.user
    order=Order.objects.all()
    return render(request, 'my_bread/order.html', {"order":order})
  
# @login_required(login_url='/accounts/login/')
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
   return render(request, 'my_bread/orderform.html', {"form": form,"order":order})    

def about(request):
    return render(request,'my_bread/aboutus.html',{})




