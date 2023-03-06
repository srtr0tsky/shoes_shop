from django.contrib import admin
from django.urls import path, include
from .views import add_to_cart, remove_from_cart, ShowItemsCart
urlpatterns = [
    path('add/<str:slug>', add_to_cart, name='add_cart'),
    path('remove/<str:slug>', remove_from_cart, name='remove_from_cart'),
    path('', ShowItemsCart.as_view(), name='view_cart')
]