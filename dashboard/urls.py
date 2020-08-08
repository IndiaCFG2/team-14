from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.chart, name='dashboard'),
    path('home/', views.home, name='home')
]

