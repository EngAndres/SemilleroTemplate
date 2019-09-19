from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^contacto$', views.make_contact, name='make_contact'),
	
	url(r'^proyectos$', views.load_projects, name='load_projects'),
	url(r'^proyecto/ver/(?P<pk>[A-Z, a-z, _, 0-9]+)/$', views.load_project, name='load_project'),
	url(r'^proyecto/editar/(?P<pk>[A-Z, a-z, _, 0-9]+)/$', views.edit_project, name='edit_project'),
	url(r'^proyecto/agregar/(?P<pk>[A-Z, a-z, _, 0-9]+)/$', views.add_project, name='add_project'),

	url(r'^integrantes$', views.load_staff, name='load_staff'),
	url(r'^integrante/ver/(?P<pk>[A-Z, a-z, _, 0-9]+)/$', views.load_member, name='load_member'),
	url(r'^integrante/editar/(?P<pk>[A-Z, a-z, _, 0-9]+)/$', views.edit_member, name='load_project'),
	url(r'^integrante/agregar/(?P<pk>[A-Z, a-z, _, 0-9]+)/$', views.add_member, name='add_member'),

	url(r'^productos$', views.load_products, name='load_products'),
	url(r'^producto/ver/(?P<pk>[A-Z, a-z, _, 0-9]+)/$', views.load_product, name='load_product'),
	url(r'^producto/editar/(?P<pk>[A-Z, a-z, _, 0-9]+)/$', views.edit_product, name='load_product'),
	url(r'^producto/agregar/(?P<pk>[A-Z, a-z, _, 0-9]+)/$', views.add_product, name='add_product'),
]