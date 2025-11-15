from django.db import models
from django.contrib.auth.models import User
from menu.models import FoodItems

# Create your models here.
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    food=models.ForeignKey(FoodItems,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date_added=models.DateTimeField(auto_now_add=True)
