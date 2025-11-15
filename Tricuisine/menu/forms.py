from django import forms

from menu.models import Cuisines,FoodItems,Category

class CuisineForm(forms.ModelForm):
    class Meta:
        model=Cuisines
        fields="__all__"

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields="__all__"

class FoodForm(forms.ModelForm):
    class Meta:
        model=FoodItems
        fields=['name','image','description','price','cuisine']

