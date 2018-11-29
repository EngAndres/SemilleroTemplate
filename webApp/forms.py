from django import forms
from .models import Semester
from .models import Candidate

class NewCandidate(forms.ModelForm):
	temp = Semester.semester_.get_semesters()
	semesters = [] #((element[0], element[1]) for element in temp) 

	name = forms.CharField(label = "Nombre", required=True)
	email = forms.CharField(label = "Correo", required=True)
	subject = forms.CharField(label = "Asunto", required=True)
	semester = forms.ChoiceField(label = "Semestre", required=True, choices = semesters)
	message = forms.CharField(label = "Mensaje", required=True)

	class Meta:
		model = Candidate
		fields = ('name','email','subject','semester','message') 
