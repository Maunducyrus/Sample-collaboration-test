import geocoder as geocoder
from django.contrib.sites import requests
from django.shortcuts import render

# Create your views here.

def temp_here(request):
    endpoint = "https://api.open-meteo.com/v1/forecast"
    location = geocoder.ip('me').latlng
    api_request = f"{endpoint}?latitude={location[0]}&longitude={location[1]}&hourly=temperature_2m"
    return requests.get(api_request).json()

