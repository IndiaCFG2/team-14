from django.shortcuts import render
from .models import *

# Create your views here.
def chart(request):
	    #labels = []
	    #data = []

	    #queryset = School_Analysis.objects.order_by('-count')[:5]
	    #for city in queryset:
	        #labels.append(city.name)
	        #data.append(city.population)

	    return render(request, 'dashboard/maindash.html')

def home(request):
	return render(request, 'dashboard/maindash.html', {})