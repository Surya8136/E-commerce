from django.contrib import admin
from menu.models import Cuisines, FoodItems, Category

# Register your models here.
admin.site.register(Cuisines)
admin.site.register(FoodItems)
admin.site.register(Category)