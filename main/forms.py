from django.contrib.auth.forms import UserCreationForm
from account.models import User
from django import forms


# User registration forms --------------------------------------------------------------
class signinform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2','profile_image']
#---------------------------------------------------------------------------------------