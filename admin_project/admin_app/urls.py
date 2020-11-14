from django.urls import path
from .views import greeting, dict_combine, json_read

urlpatterns = [
	path('', greeting, name = 'greeting'),
	path('dict_combine/', dict_combine, name = 'combining'),
	path('json_read/', json_read, name = 'json_read'),

	]