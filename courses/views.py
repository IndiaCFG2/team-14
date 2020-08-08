from django.shortcuts import render
from dashboard.models import Course_Analysis as ca
# Create your views here.
def courseshome(request):
    #course-discriminant_analysis
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
			course = ca.objects.filter(date__iexact=date, course=course_id, week=week, Dname=Dname)

		elif request.get('date')!=None and request.get('course')!=None and request.get('week')!=None:
				date = request.get('date')
				course_id = request.get('course')
				week = request.get('week')
				course = ca.objects.filter(date__iexact=date, course=course_id, week=week)
		elif request.get('date')!=None and request.get('course')!=None :
			date = request.get('date')
			course_id = request.get('course')
			course = ca.objects.filter(date__iexact=date, course=course_id)

		elif request.get('course')!=None :
			course_id = request.get('course')
			course = ca.objects.filter(date__iexact=date, course=course_id)
    			
	return render(request, 'dashboard/maindash.html', {'course':course})
