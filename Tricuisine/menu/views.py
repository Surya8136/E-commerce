from django.shortcuts import render
from django.views import View
from menu.models import Cuisines,FoodItems, Category
# Create your views here.
class Home(View):
    def get(self,request):
        b = Cuisines.objects.all()
        context = {'cuisines': b}
        return render(request,"home.html",context)

class Cuisine(View):
    def get(self,request,i):
        if i==1:
            t=Cuisines.objects.get(id=1)
            c=Category.objects.filter(cuisines=t)
            context={'italian':t,'categories':c}

            return render(request,"italian.html",context)
        elif i==2:
            k = Cuisines.objects.get(id=2)
            c = Category.objects.filter(cuisines=k)
            context = {'cuisine': k,'categories':c}
            return render(request, "korean.html",context)
        else:
            j= Cuisines.objects.get(id=3)
            c=Category.objects.filter(cuisines=j)
            context = {'japan': j,'categories':c}
            return render(request, "japanese.html",context)
