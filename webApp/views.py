import plots
from django.shortcuts import render




# Create your views here.
def index(request):
	return render(request, 'webApp/index.html')

def make_contact(request):
	return render(request, 'webApp/contact.html')

def load_projects(request):
	return render(request, 'webApp/projects.html')

def load_project(request, id):
	data = {}
	return render(request, 'webApp/project.html', {'data' : data})

def edit_project(request, id):
	data = {}
	return render(request, 'webApp/edit_project.html', {'data' : data})

def add_project(request, id):
	data = {}
	return render(request, 'webApp/add_project.html', {'data' : data})

def load_staff(request):
	return render(request, 'webApp/staff.html')

def load_member(request, id):
	data = {}
	return render(request, 'webApp/member.html', {'data' : data})

def edit_member(request, id):
	data = {}
	return render(request, 'webApp/edit_member.html', {'data' : data})

def add_member(request, id):
	data = {}
	return render(request, 'webApp/add_member.html', {'data' : data})

def load_products(request):
	return render(request, 'webApp/products.html')

def load_product(request, id):
	data = {}
	return render(request, 'webApp/product.html', {'data' : data})

def edit_product(request, id):
	data = {}
	return render(request, 'webApp/edit_product.html', {'data' : data})

def add_product(request, id):
	data = {}
	return render(request, 'webApp/add_product.html', {'data' : data})