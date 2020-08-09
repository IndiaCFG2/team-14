from django.contrib import messages
from django.shortcuts import render
from dashboard.models import Course_Analysis as ca
from .forms import CourseAnalysisForm


# Create your views here.

def courseshome(request):
    #course-discriminant_analysis
	form = CourseAnalysisForm()	
	cc = {'count':'-1'}
	#course = ca.objects.all()
	if request.method=="POST" :
		if request.POST.get('date')!=None and request.POST.get('course')!=None and request.POST.get('week')!=None and request.POST.get('Dname')!=None :
				date = request.POST.get('date')
				course_id = request.POST.get('course')
				week = request.POST.get('week')
				Dname = request.POST.get('Dname')
				course_obj = ca.objects.get(date=date, course=course_id, week=week, Dname=Dname)
				print(course_obj.count)
				#course = ca.objects.all()
				#messages.warning(request,'The data regarding selected filters is not available at the moment :(')

				return render(request, 'courses/coursesmain.html', {'cc':course_obj, 'form':form})
		#return render(request, 'courses/coursesmain.html', {'course':course, 'form':form})	 			
	return render(request, 'courses/coursesmain.html', { 'form':form})
