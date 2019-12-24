from flask import render_template
from flask_appbuilder import ModelView
from flask_appbuilder.models.mongoengine.interface import MongoEngineInterface
from flask_appbuilder import expose, has_access, permission_name
from app import appbuilder
from .models import *

class PassengerView(ModelView):
	datamodel = MongoEngineInterface(Passenger)
	list_columns = ['name','comm', 'passport','file']

class FilesView(ModelView):
	datamodel = MongoEngineInterface(Files)
	list_columns = [
	'filename',
	'comm',
	'download'
	]

	@expose("/d/<pk>")
	def d(self, pk):
		item = self.datamodel.get(pk)
		file = item.file.read()
		mime = file[1:4].decode('utf-8').lower()
		response =  make_response(file)
		response.headers["Content-Disposition"] = "attachment"
		response.headers["Content-Type"] = "{}".format(mime)
		return response

class TravelsView(ModelView):
	datamodel = MongoEngineInterface(Travels)
	list_columns = [ 
	'where',
	'start',
	'end',
	'travellers',
	'outUK',
	'business',
	'bus',
	'train',
	'flight',
	'cruise',
	'cars',
	'hotel',
 	'completed',
	'comm'
]

class BusView(ModelView):
	datamodel = MongoEngineInterface(Bus)
	list_columns = [
	'user',
	'start', 
	'end', 
	'company', 
	'price', 
	'currency', 
	'prepaid', 
	'ResID', 
	'linked', 
	'doc', 
	#'download',
	#'file_name',
	'comm', 
	'route', 
	'depart', 
	'arrive' 	
	]

class PassengerView(ModelView):
	datamodel = MongoEngineInterface(Passenger)
	list_columns = ['name']

class ItineraryView(ModelView):
	datamodel = MongoEngineInterface(Itinerary)
	list_columns = [
	'point ',
	'start ',
	'end ',
	'doc ',
	'comm ',
	]

class ExtraView(ModelView):
	datamodel = MongoEngineInterface(Extra)
	list_columns = [
	'user ',
	'start ',
	'end ',
	'company ',
	'price ',
	'currency ',
	'prepaid ',
	'ResID ',
	'link ',
	'doc ',
	'comm ',
	'name ',
	]

class HotelView(ModelView):
	datamodel = MongoEngineInterface(Hotel)
	list_columns = [
	'user ',
	'start ',
	'end ',
	'company ',
	'price ',
	'currency ',
	'prepaid ',
	'ResID ',
	'link ',
	'doc ',
	'comm ',
	'name ',
	'address ',
	'GPS ',
	]

class FlightsView(ModelView):
	datamodel = MongoEngineInterface(Flights)
	list_columns = [
	'user ',
	'start ',
	'end ',
	'company ',
	'price ',
	'currency ',
	'prepaid ',
	'ResID ',
	'link ',
	'doc ',
	'comm ',
	'flight ',
	'depart ',
	'arrive '
	]

class TrainView(ModelView):
	datamodel = MongoEngineInterface(Train)
	list_columns = [
	'user ',
	'start ',
	'end ',
	'company ',
	'price ',
	'currency ',
	'prepaid ',
	'ResID ',
	'link ',
	'doc ',
	'comm ',
	'route ',
	'depart ',
	'arrive ',
	]

class CruiseView(ModelView):
	datamodel = MongoEngineInterface(Cruise)
	list_columns = [
	'user',
	'start', 
	'end', 
	'company', 
	'price', 
	'currency', 
	'prepaid', 
	'ResID', 
	'link', 
	'doc', 
	'comm', 
	'cruise', 
	'depart', 
	'arrive', 	
	'itinerary', 
	'extra', 
	'agent' 
	]

class CarsView(ModelView):
	datamodel = MongoEngineInterface(Cars)
	list_columns = [
	'user ',
	'start ',
	'end ',
	'company ',
	'price ',
	'currency ',
	'prepaid ',
	'ResID ',
	'link ',
	'doc ',
	'comm ',
	#'insurance ',
	'deposit ',
	#'scan ',
	'depart ',
	'arrive ',		
	'provider '
	]

	#related_views = [PassengerView]


"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404


appbuilder.add_view(TravelsView,"TravelsView",icon="fa-folder-open-o",category="Travels")
appbuilder.add_separator("Travels")
appbuilder.add_view(PassengerView,"Passengers",icon="fa-folder-open-o",category="Travels")
appbuilder.add_view(FilesView,"Files",icon="fa-folder-open-o",category="Travels")
appbuilder.add_view(BusView,"Bus",icon="fa-dashboard",category="Travels")
appbuilder.add_view(TrainView,"Train",icon="fa-dashboard",category="Travels")
appbuilder.add_view(CruiseView,"Cruise",icon="fa-dashboard",category="Travels")
appbuilder.add_view(CarsView,"Cars",icon="fa-dashboard",category="Travels")
appbuilder.add_view(HotelView,"Hotel",icon="fa-dashboard",category="Travels")
appbuilder.add_view(FlightsView,"Flights",icon="fa-dashboard",category="Travels")

appbuilder.add_view(ItineraryView,"Itinerary",icon="fa-dashboard",category="Travels")
appbuilder.add_view(ExtraView,"Extra",icon="fa-dashboard",category="Travels")



