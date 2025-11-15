from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from shop.models import Category, Product

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class CategoriesForm(forms.ModelForm):
    class Meta:
        model= Category
        fields= "__all__"

class ProductsForm(forms.ModelForm):
    class Meta:
        model= Product
        fields = ['image','name','price','description','stock','category']

class StockForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['stock']
