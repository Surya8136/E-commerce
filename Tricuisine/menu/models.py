from django.db import models
from django.db.models import ForeignKey


# Create your models here.
class Cuisines(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="category")
    description=models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name=models.CharField(max_length=100)
    cuisines=models.ForeignKey(Cuisines,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class FoodItems(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="fooditems")
    price=models.IntegerField()
    description=models.TextField()
    cuisine=ForeignKey(Cuisines,on_delete=models.CASCADE,related_name="foods")
    category=ForeignKey(Category,on_delete=models.CASCADE,related_name="food")
    avg_rating=models.FloatField(default=0.0)


    def __str__(self):
        return self.name
