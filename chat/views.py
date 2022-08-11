from django.shortcuts import render, redirect
from .forms import signinform,customerform
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Customer
from django.contrib.auth.models import User
from django.contrib import messages
import os

# Create your views here.
def index(request):
    return render(request,'chat/index.html')
def login(request):
    return render(request,'chat/login.html')
def signin(request):
    form1 = signinform()
    context = {'form1':form1}

    if request.method == 'POST':
        form1 = signinform(request.POST)
        
        if form1.is_valid():
            newuser = form1.save()
            newuserdata = form1.cleaned_data
            newcustomer = Customer()    
            newcustomer.user = User.objects.get(id=newuser.id)
            newcustomer.email = newuserdata['email']
            newcustomer.name = newuserdata['username']
            newcustomer.save()
            messages.info(request, "Thanks for registering. You are now logged in.")
            auth_login(request, newuser)
            return redirect(os.path.join('profile/',str(newcustomer.id)))
    return render(request,'chat/signin.html',context)

@login_required
def profile(request,pk):
    newcustomer = Customer.objects.get(id=pk)
    form2 = customerform(instance=newcustomer)
    context = {'form2':form2}
    if request.method == 'POST':
        form2 = customerform(request.POST,request.FILES,instance=newcustomer)
        if form2.is_valid():
            form2.save()
            return redirect('/friends/')

    return render(request,'chat/profile.html',context)

def friends(request):
    return render(request,'chat/friends.html')