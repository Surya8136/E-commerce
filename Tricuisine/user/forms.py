from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password1','password2']


class Login(forms.ModelForm):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

