from django.shortcuts import render
from django.views import View
from shop.models import Product
from django.db.models import Q
# Create your views here.
class Search(View):
    def get(self, request):
        s=request.GET['s']
        print(s)
        if s:
            p=Product.objects.filter(Q(name__icontains=s)|Q(description__icontains=s)|Q(price__icontains=s))
            context={'search':p}
            return render(request,"search.html",context)