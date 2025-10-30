from django.shortcuts import render
from django.views import View
from shop.models import Category
# Create your views here.

class Categories(View):
    def get(self,request):
        b=Category.objects.all()
        context={'category':b}
        return render(request,"categories.html",context)

class Products(View):
    def get(self,request,i):
        c=Category.objects.get(id=i)
        context={'category':c}
        return render(request,"products.html",context)