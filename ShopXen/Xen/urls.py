from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('cat/<int:category_id>', product_detail, name='product_detail'),
    path('/product/<int:product_id>', preSales, name='preSales'),

]
