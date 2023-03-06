from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView
from .views import MainPage, DetailProduct
urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('detail-product/<str:slug>', DetailProduct.as_view(), name='detail_product'),

]