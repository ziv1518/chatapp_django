from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer

# User registration forms --------------------------------------------------------------
class signinform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class customerform(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','phone','profile_image']
#---------------------------------------------------------------------------------------