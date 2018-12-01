from bokeh.plotting import figure 
from bokeh.embed import components

from bokeh.core.properties import value
from bokeh.models import ColumnDataSource
from bokeh.transform import dodge


def plot_members():
	years = [str(i) for i in range(2016,2020)] #[2016,2017,2018,2019]
	states = ['Activos', 'Graduados', 'Retirados']
	
	active = [6, 10, 17, 21]
	graduated = [6, 10, 17, 21]
	retired = [2, 1, 1, 1] 

	data_ = {'years' : years, 'Activos' : active, 'Graduados' :  graduated, 'Retirados' : retired}
	source_ = ColumnDataSource(data= data_)

	title_ = "Miembros del Semillero"
	x_axis_ = "Años"
	y_axis_ = "Miembros"
	width_ = 500
	height_ = 350

	plot = figure(title= title_, x_axis_label= x_axis_, x_range= years, y_axis_label= y_axis_, y_range= (0,25), plot_width= width_,  plot_height= height_)	
	
	plot.vbar(x=dodge('years', -0.25, range=plot.x_range), top='Activos', width=0.2, source= source_, color="#FF8800", legend=value("Activos"))
	plot.vbar(x=dodge('years', 0.0, range=plot.x_range), top='Graduados', width=0.2, source= source_, color="#00FF88", legend=value("Graduados"))
	plot.vbar(x=dodge('years', 0.25, range=plot.x_range), top='Retirados', width=0.2, source= source_, color="#8800FF", legend=value("Retirados"))

	plot.legend.location = "top_left"	
	plot.legend.orientation = "horizontal"	
	plot.xgrid.grid_line_color = None

	script, div = components(plot)
	graphic = {"script_members" : script, "div_members" : div}

	return graphic



def plot_production():
	years = [str(i) for i in range(2016,2020)] #[2016,2017,2018,2019]
	papers = [0, 3, 2, 8]	
	events = [1, 4, 3, 10]
	total_papers = sum(papers)	
	total_events = sum(events)	
	total_production = total_events + total_papers
	

	title_ = "Producción del Semillero"
	x_axis = "Años"
	y_axis = "Productos"
	width = 500
	height = 350

	plot = figure(title= title_,  x_axis_label= x_axis, x_range= years, y_axis_label= y_axis, plot_width= width,  plot_height= height)
	plot.line(years, papers, legend= 'Artículos', line_width = 2, color='#FF00FF')
	plot.line(years, events, legend= 'Eventos', line_width = 2, color='#00FFFF')
	
	plot.x_range.range_padding = 1

	script_, div_ = components(plot)
	graphic = {"script_production" : script_, "div_production" : div_, "production" : total_production, "events" : total_events, "papers" : total_papers}

	return graphic





