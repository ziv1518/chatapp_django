from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer

# User registration forms --------------------------------------------------------------
class signinform(UserCreationForm):
    required_css_class = 'required-field'
    error_css_class = 'error-field'
    error_messages = {
        'password_mismatch': "The password is not the same",
        
    }
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        error_messages = {
            'email': {
                'invalid_email': 'The email address is invalid.',
            },
        }
     
class customerform(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','phone','profile_image']
#---------------------------------------------------------------------------------------
