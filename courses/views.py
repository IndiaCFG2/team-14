from django.contrib.messages.context_processors import messages
from django.shortcuts import render

from dashboard.models import Course_Analysis as ca

from .forms import CourseAnalysisForm


# Create your views here.
def courseshome(request):
    #course-discriminant_analysis
	form = CourseAnalysisForm()	
	course = ca.objects.all()
	if request.method=="POST" :
		date=""
		course=0
		week=0
		Dname=0
		if request.get('date')!=None and request.get('course')!=None and request.get('week')!=None and request.get('Dname')!=None :
			date = request.get('date')
			course_id = request.get('course')
			week = request.get('week')
			Dname = request.get('Dname')
			try:
				course = ca.objects.filter(date__iexact=date, course=course_id, week=week, Dname=Dname)
			except:
				course = ca.objects.all()
				messages.warning(request,'The data regarding selected filters is not available at the moment :(')

			return render(request, 'dashboard/maindash.html', {'course':course, 'form':form})

		elif request.get('date')!=None and request.get('course')!=None and request.get('week')!=None:
				date = request.get('date')
				course_id = request.get('course')
				week = request.get('week')
				try:
					course = ca.objects.filter(date__iexact=date, course=course_id, week=week)
				except:
					course = ca.objects.all()
					messages.warning(request,'The data regarding selected filters is not available at the moment :(')
				return render(request, 'dashboard/maindash.html', {'course':course, 'form':form})

		elif request.get('date')!=None and request.get('course')!=None :
			date = request.get('date')
			course_id = request.get('course')
			try:
				course = ca.objects.filter(date__iexact=date, course=course_id)
			except:
				course = ca.objects.all()
				messages.warning(request,'The data regarding selected filters is not available at the moment :(')

			return render(request, 'dashboard/maindash.html', {'course':course, 'form':form})

		elif request.get('course')!=None :
			course_id = request.get('course')
			try:
				course = ca.objects.filter(date__iexact=date, course=course_id)
			except:
				course = ca.objects.all()
				messages.warning(request,'The data regarding selected filters is not available at the moment :(')

			return render(request, 'dashboard/maindash.html', {'course':course, 'form':form})
		else :
			messages.warning(request,'Please select applicable fields to show statistics')
			return render(request, 'dashboard/maindash.html', {'course':course, 'form':form})
    			
	return render(request, 'dashboard/maindash.html', {'course':course, 'form':form})
