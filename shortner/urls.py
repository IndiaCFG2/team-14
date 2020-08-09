from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('<str:token>', views.Home, name='Home'),
    path('', views.Make, name='Make New'),  
]
