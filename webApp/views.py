from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'webApp/index.html')

def makeContact(request):
	return render(request, 'webApp/contacto.html')

def loadProjects(request):
	return render(request, 'webApp/proyectos.html')

def viewStaff(request):
	return render(request, 'webApp/integrantes.html')
