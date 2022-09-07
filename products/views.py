from django.shortcuts import render
from .models import Products 

# Create your views here.

def products_list(request):
    products = Products.objects.all()

    return render(request , "products/products_list.html",{'products':products})

def product_detail(request,id):
    product = Products.objects.get(id=id)

    return render(request,'products/product_detail.html',{'product':product})

