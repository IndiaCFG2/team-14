from django.shortcuts import render

# Create your views here.
def courseshome(request):
	return render(request, 'dashboard/maindash.html', {})