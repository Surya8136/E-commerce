from django.shortcuts import render,redirect
from django.views import View
from shop.models import Product
from cart.models import Cart,Order,Order_items
from cart.forms import OrderForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login
import uuid

import razorpay

# Create your views here.
class AddtoCart(View): #add items to cart
    def get(self,request,i):
        p=Product.objects.get(id=i)             #get the product table detail according to id=i
        u=request.user                          #get the user detail
        try:
            c=Cart.objects.get(user=u,product=p) #checks whether the product already placed by the current user or checks whether the product is there in the Cart table
            c.quantity+=1                        #if yes increments the quantity by 1
            c.save()                             #save
        except:
            c=Cart.objects.create(user=u,product=p,quantity=1) #else create a new cart record inside Cart table
            c.save()
        return redirect('cart:cartview')


class CartView(View):#display items
    def get(self,request):
        u=request.user
        c=Cart.objects.filter(user=u) #filters the cart items selected by current user
        total=0
        for i in c:
            total+=i.product.price * i.quantity
        context={"cart":c,"total":total}
        return render(request,"cart.html",context)

class Cartdecrement(View):
    def get(self,request,i): #product id in cart
        p=Product.objects.get(id=i)
        u=request.user
        try:
            c=Cart.objects.get(user=u,product=p)
            if(c.quantity > 1):
                c.quantity-=1
                c.save()
            else:
                c.delete()
        except:
            pass
        return redirect('cart:cartview')

class Cartremove(View):
    def get(self,request,i): #product id in cart
        p=Product.objects.get(id=i)
        u=request.user
        try:
            c=Cart.objects.get(user=u,product=p)
            c.delete()
        except:
            pass

        return redirect('cart:cartview')


def checkstock(c):
    for i in c:
        p=i.product
        if i.quantity > p.stock :
            return False
        return True
class CheckoutView(View):
    def get(self,request):
        u=request.user
        c=Cart.objects.filter(user=u)
        stock=checkstock(c)
        if stock:
            form_instance=OrderForm()
            context={"form":form_instance,"stock_available": True}
            return render(request,"checkout.html",context)
        else:
            messages.error(request,"Can't Place Order")
            context={"stock_available": False}
            return render(request, "checkout.html",context)

    def post(self,request):
        form=OrderForm(request.POST)
        if form.is_valid():
            o=form.save(commit=False)       #if you want to add other items to the record,set commit= False. here we only displayed address,payment method and phone number,we need all details to store in the table
            u=request.user  #current user
            o.user=u    #add user to the record
            c=Cart.objects.filter(user=u)  #current cart
            total=0
            for i in c:
                total += i.product.price * i.quantity           #subtotal function is defined inside the models.py of cart, so it can be called,no need to display everytime by equation
            o.amount=total
            o.save()
            #payment method razorpay demo
            if o.payment_method=="online":
                # Razorpay client connection    'key id'                  'secret'
                client=razorpay.Client(auth=('rzp_test_RdkVPgll1oDuuG','5d632b7aark4aAq6GtARc7Zz'))
                #place order - currency will be in paisa,so to print in rupees multiply with 100
                response_payment=client.order.create(dict(amount=total*100,currency="INR"))
                print(response_payment)

                #savve the id in the order table
                id=response_payment['id']   # get the id from the above dictionary called response_payment
                o.order_id=id
                o.save()
                context={'payment':response_payment}
                return render(request, "payment.html", context)
            else: #ORDER COD
                o.is_ordered=True
                #to create order id manually -UUID-used to create unique ids
                #uuid.uuid4() - a long number with alphabets
                #uuid.uuid4().hex[:14] -get 14 characters
                #order+uuid.uuid4().hex[:14]

                uid=uuid.uuid4().hex[:14]
                id='order_COD'+uid
                o.order_id=id
                o.save()
                c=Cart.objects.filter(user=u)
                for i in c:
                    items=Order_items.objects.create(order=o,product=i.product,quantity=i.quantity)
                    items.save()
                    items.product.stock-=items.quantity
                    items.product.save()

                c.delete()





                return render(request,"payment.html")


#After payment completion razorpay redirects into payment_success view
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
@method_decorator(csrf_exempt,name="dispatch")        #to avoid csrf verification- csrf is used to check whether the post request comes from the same domain
class Payment_success(View):
    def post(self,request,i):       #i is the username, after the payment (razorpay) user will be logged out. To change that to login we use the code below
        print(i)
        u=User.objects.get(username=i)  #get the username from the user model
        login(request,u)                #login with the current user

        response=request.POST           # after payment razorpay sends payment details into success view as response
        print(response)
        id=response[ 'razorpay_order_id']
        print(id)



# after placing order
        # save the details to order table
        o=Order.objects.get(order_id=id)
        o.is_ordered=True  #after successful completion of order
        o.save()

        # Then to order_items table
        c=Cart.objects.filter(user=u)
        for i in c:
            print(i)
            items=Order_items.objects.create(order=o,product=i.product,quantity=i.quantity)
            items.save()
            items.product.stock-=items.quantity
            items.product.save()
        #delete cart items
        c.delete()
        return render(request, "payment_success.html")


class YourOrders(View):
    def get(self,request):
        u=request.user
        o=Order.objects.filter(user=u,is_ordered=True)
        context={"order":o}
        return render(request,"yourorders.html",context)