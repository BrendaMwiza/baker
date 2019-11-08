from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def page(request):
    current_user = request.user
    return render(request,'all-pages/index.html',{})

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