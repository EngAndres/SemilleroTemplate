from django.shortcuts import render

from bokeh.plotting import figure 
from bokeh.embed import components

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
	years = [i for i in range(2016,2020)] #[2016,2017,2018,2019]
	active = [6, 10, 17, 21]
	graduated = [6, 10, 17, 21]
	retired = [2, 1, 1, 1]
	
	papers = [0, 3, 2, 8]	
	events = [1, 4, 3, 10]

	title_plot_1 = "Miembros del Semillero"
	x_axis = "Años"
	y_axis_1 = "Miembros"
	plot_1_width = 500
	plot_1_height = 350

	title_plot_2 = "Producción del Semillero"
	y_axis_2 = "Productos"
	plot_2_width = 500
	plot_2_height = 350

	plot_1 = figure(title= title_plot_1,  x_axis_label= x_axis, y_axis_label= y_axis_1, plot_width= plot_1_width,  plot_height= plot_1_height)
	plot_2 = figure(title= title_plot_2,  x_axis_label= x_axis, y_axis_label= y_axis_2, plot_width= plot_2_width,  plot_height= plot_2_height)
	
	plot_1.circle(years, active)
	plot_1.line(years, active, legend= '', line_width = 2)

	plot_2.line(years, papers, legend= 'Artículos', line_width = 2)
	
	#Store components 
	script_1, div_1 = components(plot_1)
	script_2, div_2 = components(plot_2)


	return render(request, 'webApp/integrantes.html', {'script_plot_1' : script_1, 'div_plot_1' : div_1, 'script_plot_2' : script_2, 'div_plot_2' : div_2})



