from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def product(request):
    items = Product.objects.all()
    context = {
        'items': items
    }
    return render(request,'product/product.html',context)

def ful_product(request,my_id):
    item = Product.objects.get(id=my_id)
    context = {
        'item': item
    }

    return render(request,'product/detail.html',context = context)


def contact(request):
    return render(request,'product/contacts.html')