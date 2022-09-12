from django.shortcuts import render, redirect
from .forms import signinform
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def index(request):
    return render(request,'main/index.html')
def login(request):
    return render(request,'main/login.html')
#-------------------------------------------------------------------------------------------------
class signinview(generic.FormView):
    template_name = 'main/signin.html'
    form_class = signinform 
    success_url = '/friends'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class loginview(generic.FormView):
    template_name = 'main/login.html'
    form_class = AuthenticationForm
    success_url = '/friends'

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return super().form_valid(form)


#-------------------------------------------------------------------------------------------------
def friends(request):
    return render(request,'main/friends.html')