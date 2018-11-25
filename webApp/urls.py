from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^contact/$', views.makeContact, name='make_contact'),
	url(r'^projects/$', views.loadProjects, name='load_projects'),
	url(r'^staff/$', views.viewStaff, name='view_staff'),
]
