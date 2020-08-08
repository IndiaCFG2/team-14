from django import forms
from dashboard.models import Course_Analysis

class CourseAnalysisForm(forms.ModelForm):
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}))
    class Meta:
        model = Course_Analysis
        fields = ('date', 'course', 'week', 'Dname')
        labels = {
            'date':'Date', 'course' : 'Course Name', 'week' : 'Week of the course', 'Dname' : 'Day of the week of course'
        }