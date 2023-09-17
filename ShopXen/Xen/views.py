from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import *
# Create your views here.
def home(request):
    category = Category.objects.all()
    return render(request, 'Xen/store.html', {'categories':category})


def product_detail(request, category_id):
    category = Category.objects.get(category_id=category_id)
    products = category.product_set.all() 
    return render(request, 'Xen/product_details.html', {'products':products})


def preSales(request, product_id):
    product = Product.objects.get(product_id=product_id)
    print(product)
    return render(request, 'Xen/presales.html', {'product':product})
