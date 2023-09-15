from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('checkout/', checkout, name='checkout'),
    path('product/<str:pname>/', product, name='product'),
]
