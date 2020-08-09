#from django.contrib.messages.context_processors import messages
from django.shortcuts import render

from dashboard.models import School_Analysis as sa

from .forms import SchoolAnalysisForm,schoolDayAnalysisForm
from django.contrib import messages
import json
from datetime import datetime, timedelta


def schoolhome(request):
	form = SchoolAnalysisForm()	
	schoolvar=""
	label=[]
	count=[]
	if request.method=="POST" :
		date = request.POST.get('date')
		schoolvar = sa.objects.filter(date__iexact=date)
		for school1 in schoolvar:
			label.append(school1.school)
			count.append(school1)
			# today = date.today()
			# school = sa.objects.filter(date_year=today.year, datemonth=today.month, date_day=today.day)
		# except:
		# 	print('nto working1')
		# 	school = sa.objects.all()
			# messages.warning(request,'The data regarding selected filters is not available at the moment :(')
	return render(request, 'schools/schoolsmain.html', {'label':label, 'count':count, 'form':form})

#reate your views here.
def schoolDayAnalysis(request):
    #school-discriminant_analysis
	form = schoolDayAnalysisForm()	
	school1=""
	course = sa.objects.all()
	if request.method=="POST" :
		# count=0
		# if request.POST.get('count')!=None and request.POST.get('school')!=None:
		# 	count = request.POST.get('count')
		# 	school_id = request.POST.get('school')
		# 	try:
		# 		school = School_Analysis.objects.filter(since=since).order_by('-id')[:count][::-1]
		# 		print(school)

		# 	except:
		# 		school = sa.objects.all()
		# 		messages.warning(request,'The data regarding selected filters is not available at the moment :(')
		if request.POST.get('school')!=None:
			school_id = request.POST.get('school')
			# school1 = sa.objects.filter(since=since, school = school_id).order_by('-date')[:10][::-1]
			how_many_days = 7
			school1 = sa.objects.filter(date__gte=datetime.now()-timedelta(days=how_many_days),school=school_id)
			print(school1)
			return render(request, 'schools/schoolsmain.html', {'school':school1, 'form':form})
	return render(request, 'schools/schoolsmain.html', {'school':school1, 'form':form})