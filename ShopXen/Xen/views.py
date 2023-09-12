from django.shortcuts import render




def home(request):
    return render(request, 'Xen/store.html', {})

def checkout(request):
    return render(request, 'Xen/checkout.html', {})


