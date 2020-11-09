from django.urls import path
from .views import greeting, introduction,date_time, dict_sq, location

urlpatterns = [
    path('',greeting, name = "greeting"),
    path('introduction/',introduction, name = "introduction"),
    path('date/time/', date_time, name = "date_and_time"),
    path('dict/', dict_sq, name = "dictionary"),
    path('location/', location, name = "geolocation"),

    ]
