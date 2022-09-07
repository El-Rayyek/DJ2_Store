from django.urls import path
from .views import products_list , product_detail

app_name = 'products'


urlpatterns = [
   path('',products_list,name='product_list'),
   path('detail/',product_detail,name='product_detail')
]