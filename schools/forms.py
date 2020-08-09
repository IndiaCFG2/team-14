from django import forms
from dashboard.models import School_Analysis
from .models import Boards

class SchoolAnalysisForm(forms.ModelForm):
	#options = Boards.objects.all()
    #Boards = ModelChoiceField(queryset=options, to_field_name='board_name', empty_label="None")
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}))
    #count = forms.IntegerField()
    class Meta:
        model = School_Analysis
        fields = ('date',)
        labels = {
        	 'date' : 'Date'
        }

class schoolDayAnalysisForm(forms.ModelForm):
    #options = Boards.objects.all()
    #Boards = ModelChoiceField(queryset=options, to_field_name='board_name', empty_label="None")
    #date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}))
    #count = forms.IntegerField()
    class Meta:
        model = School_Analysis
        fields = ('school',)
        labels = {
             'school' : 'School'
        }