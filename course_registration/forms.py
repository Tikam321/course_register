from django.contrib.auth.forms import  UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Course_Registration

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model =  User
        fields = ['username','email','password1','password2']
