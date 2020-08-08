from django.shortcuts import render

# Create your views here.
from schools.models import Schools
# Create your views here.

def schools(request):
    school = Schools.objects.all()
    context ={'school',school}
    return render(request, 'schools.html')