from django.shortcuts import render, redirect
from .forms import signinform
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'main/index.html')
def login(request):
    return render(request,'main/login.html')
#-------------------------------------------------------------------------------------------------
'''signin() and profile() serves as a set for user registration. signin create a user model which 
only takes the username, email, and passwoed. After the user is created, it will auto-login and 
pass the user to create a customer model, which serves as a customer profile that take the
display name, phone, and profile image.
'''
def signin(request):
    form1 = signinform()
    context = {'form1':form1}

    if request.method == 'POST':
        form1 = signinform(request.POST)
        
        if form1.is_valid():
            newuser = form1.save()
            messages.info(request, "Thanks for registering. You are now logged in.")
            auth_login(request, newuser)
            return redirect('/friends')
    return render(request,'main/signin.html',context)

#-------------------------------------------------------------------------------------------------
def friends(request):
    return render(request,'main/friends.html')