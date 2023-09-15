from django.shortcuts import render


from .models import Product

def home(request):
    products = Product.objects.all()
    
    return render(request, 'Xen/store.html', {'products': products})

def checkout(request):
    return render(request, 'Xen/checkout.html', {})

def product(request, pname):
    return render(request, 'Xen/product_info.html', {'pname':pname})

