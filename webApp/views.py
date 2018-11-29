from django.shortcuts import render
from .models import Candidate
from .models import Semester
from .forms import NewCandidate



# Create your views here.
def index(request):
	return render(request, 'webApp/index.html')

def makeContact(request):
	if request.method == 'POST':
		frmNewCandidate = NewCandidate(request.POST)

		if frmNewCandidate.is_valid():
			candidate = frmNewCandidate.save(commit = False)
			candidate.semester_fk = Semester.objects.get(id_semester = request.POST.get("semester"))
			candidate.save()
		
	frmNewCandidate = NewCandidate()
	return render(request, 'webApp/contacto.html', {'frmNewCandidate':frmNewCandidate})

def loadProjects(request):
	return render(request, 'webApp/proyectos.html')

def viewStaff(request):
	return render(request, 'webApp/integrantes.html')
