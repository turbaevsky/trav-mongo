from mongoengine import Document
from flask import Markup, url_for, send_file
from mongoengine import (DateTimeField, StringField, ReferenceField, ListField, BooleanField, IntField,
FloatField, URLField, GeoPointField, EmailField, FileField, EmbeddedDocumentField, EmbeddedDocument,
GenericReferenceField)
import re, logging
from flask import make_response, Response

'''
	def __unicode__(self):
		return self.name

	def __repr__(self):
		return self.name

	def __str__(self):
		return self.name

'''
class Files(Document):
	file = FileField()
	filename = StringField()
	comm = StringField()

	def __unicode__(self):
		return '{}: {}'.format(self.filename, self.comm)

	def download(self):
		file = self.file.read()
		if file is not None:
			mime = file[1:4].decode('utf-8').lower()
			return Markup('<a href="' + url_for("FilesView.d", pk=str(self.id)) + '">Download as {}</a>'.format(mime))


class Passenger(Document):
	name = StringField()
	comm = StringField()
	file = ReferenceField(Files)
	passport = StringField()

	def __unicode__(self):
		return self.name


class Itinerary(Document):
	point = StringField()
	start = DateTimeField()
	end = DateTimeField()
	doc = ReferenceField(Files)
	comm = StringField()

	def __unicode__(self):
		return 'Rec {} {} {}'.format(self.comm, self.start, self.point)


class Extra(Document):
	user = ListField(ReferenceField(Passenger))
	start = DateTimeField()
	end = DateTimeField()
	company = StringField()
	price = FloatField()
	currency = StringField()
	prepaid = BooleanField()
	ResID = StringField()
	link = StringField()
	doc = ListField(ReferenceField(Files))
	comm = StringField()
	name = StringField()

	def __unicode__(self):
		return 'Rec {} {} {}'.format(self.comm, self.start, self.name)


class Hotel(Document):
	user = ListField(ReferenceField(Passenger))
	start = DateTimeField()
	end = DateTimeField()
	company = StringField()
	price = FloatField()
	currency = StringField()
	prepaid = BooleanField()
	ResID = StringField()
	link = StringField()
	doc = ListField(ReferenceField(Files))
	comm = StringField()
	name = StringField()
	address = StringField()
	GPS = StringField()

	def __unicode__(self):
		return '{} to {}: {} recId {}'.format(self.start, self.end, self.name, self.comm)


class Flights(Document):
	user = ReferenceField(Passenger)
	start = DateTimeField()
	end = DateTimeField()
	company = StringField()
	price = FloatField()
	currency = StringField()
	prepaid = BooleanField()
	ResID = StringField()
	link = StringField()
	doc = ReferenceField(Files)
	comm = StringField()
	flight = StringField()
	depart = StringField()
	arrive = StringField()

	def __unicode__(self):
		return 'RecId {}: {} to {} on {}: {}'.format(self.comm, self.depart, self.arrive, self.start, self.flight)

	def __repr__(self):
		return self.flight

	#def __str__(self):
#		return self.flight


class Bus(Document):
	user = ListField(ReferenceField(Passenger))
	start = DateTimeField()
	end = DateTimeField()
	company = StringField()
	price = FloatField()
	currency = StringField()
	prepaid = BooleanField()
	ResID = StringField()
	link = StringField()
	doc = ReferenceField(Files)
	comm = StringField()
	route = StringField()
	depart = StringField()
	arrive = StringField()	

	def __unicode__(self):
		return 'RecId {} to {} on {}: {}'.format(self.comm, self.depart, self.arrive, self.start, self.route)

	def linked(self):
		return Markup('<a href="' + self.link + '">Download</a>') if re.search(r'^http*',self.link) else None


class Train(Document):
	user = ListField(ReferenceField(Passenger))
	start = DateTimeField()
	end = DateTimeField()
	company = StringField()
	price = FloatField()
	currency = StringField()
	prepaid = BooleanField()
	ResID = StringField()
	link = StringField()
	doc = ListField(ReferenceField(Files))
	comm = StringField()
	route = StringField()
	depart = StringField()
	arrive = StringField()

	def __unicode__(self):
		return 'RecId {} {} to {} on {}: {}'.format(self.comm, self.depart, self.arrive, self.start, self.route)


class Cruise(Document):
	user = ListField(ReferenceField(Passenger))
	start = DateTimeField()
	end = DateTimeField()
	company = StringField()
	price = FloatField()
	currency = StringField()
	prepaid = BooleanField()
	ResID = StringField()
	link = StringField()
	doc = ListField(ReferenceField(Files))
	comm = StringField()
	cruise = StringField()
	depart = StringField()
	arrive = StringField()	
	itinerary = ListField(ReferenceField(Itinerary))
	extra = ListField(ReferenceField(Extra))
	agent = StringField()

	def __unicode__(self):
		return '{} to {} on {}: {} recId {}'.format(self.depart, self.arrive, self.start, self.cruise, self.comm)


class Cars(Document):
	user = ReferenceField(Passenger)
	start = DateTimeField()
	end = DateTimeField()
	company = StringField()
	price = FloatField()
	currency = StringField()
	prepaid = BooleanField()
	ResID = StringField()
	link = StringField()
	doc = ListField(ReferenceField(Files))
	comm = StringField()
	deposit = FloatField()
	depart = StringField()
	arrive = StringField()		
	provider = StringField()

	def __unicode__(self):
		return '{} to {} on {}: {} recId {}'.format(self.depart, self.arrive, self.start, self.company, self.comm)

class Travels(Document):
	where = StringField()
	start = DateTimeField()
	end = DateTimeField()
	docs = ListField(ReferenceField(Files))
	outUK = BooleanField()
	business = BooleanField()
	bus = ListField(ReferenceField(Bus))
	train = ListField(ReferenceField(Train))
	flight = ListField(ReferenceField(Flights))
	cruise = ListField(ReferenceField(Cruise))
	cars = ListField(ReferenceField(Cars))
	hotel = ListField(ReferenceField(Hotel))
	travellers = ListField(ReferenceField(Passenger))
	completed = BooleanField()
	comm = StringField()

