from django.contrib import admin
from django.urls import path, include
from .views import RegisterUser

urlpatterns = [
    path('', RegisterUser.as_view(), name='sign_up'),

]