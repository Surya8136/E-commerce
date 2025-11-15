from datetime import timezone

from django.db import models
from django.contrib.auth.models import User
from shop.models import Product

# Create your models here.
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


    def subtotal(self):   #self means current cart object
        return self.product.price * self.quantity

from django.utils import timezone
class Order(models.Model): #order details
    amount=models.IntegerField(null=True)
    order_id=models.CharField(max_length=100,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.IntegerField()
    address=models.TextField()
    ordered_date = models.DateTimeField(auto_now=True)
    payment_method = models.CharField(max_length=100)
    is_ordered=models.BooleanField(default=False)
    delivery_status=models.CharField(default="Pending")

    def __str__(self):
        return self.user.username

class Order_items(models.Model):#order product details
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='product')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="products")
    quantity=models.IntegerField()

    def __str__(self):
        return self.product.name