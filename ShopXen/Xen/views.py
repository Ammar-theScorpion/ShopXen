from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'Xen/store.html', {'products':products})