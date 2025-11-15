from django.shortcuts import render,redirect
from cart.models import Cart
from menu.models import FoodItems
from django.views import View
# Create your views here.

class AddToCart(View):
    def get(self,request,i):
        f=FoodItems.objects.get(id=i)
        u=request.user
        try:
            c=Cart.objects.filter(user=u,food=f)
            c.quantity+=1
            c.save()
        except:
            c=Cart.objects.create(user=u,food=f,quantity=1)
            c.save()
        return redirect('cart:cartview')

class MinusCart(View):
    def get(self,request,i):
        f=FoodItems.onjects.get(id=i)
        u=request.user
        try:
            c=Cart.onjects.filter(user=u,food=f)
            c.quantity-=1
            c.save()
        except:
            pass

        return redirect('cart:cartview')

class CartView(View):
    def get(self,request):
        u=request.user
        c=Cart.objects.filter(user=u)
        context={'cart':c}
        return render(request,"CartView.html",context)
