from django.urls import path, include
from . import views

app_name = 'schools'
urlpatterns = [
    path('', views.schoolhome, name='schoolshome'),
    path('dayanalysis/', views.schoolDayAnalysis, name='dayanalysis')

]