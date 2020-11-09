from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import geocoder

# Create your views here.


def greeting(request):
	return HttpResponse("Hello!!! Good to see you hear!!!")

def introduction (request):
	return HttpResponse("I'm Nazeli and this is my first django app!!!")

def date_time(request):
	now =datetime.now()
	return HttpResponse	(F"Current date and time is {now}")

def dict_sq(request):
	d = dict()
	for i in range(1,16):
		d[i] = i * i 

	return HttpResponse(F"This is a SPECIAL dictionary :D {d}")

def location(request):
	g = geocoder.ip('me')
	return HttpResponse(F"This is you geocordinate {g.latlng}. Can't convert it yet, but you're probably in Yerevan :D")



