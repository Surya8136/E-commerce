from django.shortcuts import render,redirect
from django.views import View
from shop.models import Category, Product
from shop.forms import RegisterForm, LoginForm ,ProductsForm ,CategoriesForm, StockForm
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
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

class ProductDetail(View):
    def get(self,request,i):
        p=Product.objects.get(id=i)
        context={'products':p}
        return render(request,"productdetail.html",context)

class Register(View):
    def get(self,request):
        form=RegisterForm()
        context={'form':form}
        return render(request,"register.html",context)
    def post(self,request):
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop:login')
        else:
            return render(request,"register.html",{'form':form})
class Login(View):
    def get(self,request):
        form=LoginForm()
        return render(request,"login.html",{'form':form})
    def post(self,request):
        form=LoginForm(request.POST)
        if form.is_valid():
            u=form.cleaned_data['username']
            p=form.cleaned_data['password']
            user=authenticate(username=u,password=p)
            if user:
                login(request,user)
                return redirect('shop:category')
            else:
                return render(request,"login.html",{'form':form})

class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('shop:category')

class AddProduct(View):
    def get(self,request):
        form=ProductsForm()
        context={'form':form}
        return render(request,"addproduct.html",context)
    def post(self,request):
        form=ProductsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop:category')




class AddCategory(View):
    def get(self, request):
        form =CategoriesForm()
        return render(request, "addcategory.html", {'form': form})

    def post(self,request):
        form =CategoriesForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop:category')
        else:
            return render(request,"addcategory.html",{'form':form})

class AddStock(View):
    def get(self,request,i):
        b=Product.objects.get(id=i)
        form=StockForm(instance=b)
        context={'form':form}
        return render(request,"addstock.html",context)
    def post(self,request,i):
        b = Product.objects.get(id=i)
        form=StockForm(request.POST,instance=b)
        if form.is_valid():
            form.save()
            return redirect('shop:category')



