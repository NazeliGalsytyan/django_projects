from django.shortcuts import render
from django.http import HttpResponse
from collections import Counter 
import os
import json

# Create your views here.

dict_ = {
		"name": "Nana",
		"surname": "Galstyan"
		}

def greeting(request):
	content = {"name": dict_}
	return render(request, "admin_app/welcome.html", content)

def dict_combine(request):
	d1 = {'a': 100, 'b': 200, 'c':300}
	d2 = {'a': 300, 'b': 200, 'd':400}
	d = Counter(d1) + Counter(d2)
	content = {'key': d}

	return render(request, "admin_app/dict.html", content)

def json_read(request):
	with open(os.path.join(os.getcwd(), "read.json"), 'r') as file:
		data = json.load(file)

		content = { "data":data}

	return render(request, "admin_app/json_read.html", content)




