from django.shortcuts import render, redirect
from .forms import signinform
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.views import generic


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
class signinview(generic.FormView):
    template_name = 'main/signin.html'
    form_class = signinform 
    success_url = '/friends'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
#-------------------------------------------------------------------------------------------------
def friends(request):
    return render(request,'main/friends.html')