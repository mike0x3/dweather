from django.shortcuts import render, redirect
from django.http import HttpResponse
from pyowm import OWM
from .weather import getWeather
from pyowm import OWM
import requests
import json
from .forms import searchCity


def index(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	form = searchCity()
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	r = requests.get(f'http://ip-api.com/json/{ip}?fields=status,message,country,countryCode,city')
	y = json.loads(r.text)
	countrycode = y['countryCode']
	country = y['country']
	city = y['city']
	temp_location = getWeather(f'{city},{countrycode}').getTemp()
	temp_milano = getWeather('Milan,IT').getTemp()
	temp_roma = getWeather('Rome,IT').getTemp()
	temp_torino = getWeather('Turin,IT').getTemp()
	stato_torino = getWeather('Turin,IT').getStatus()
	stato_roma = getWeather('Rome,IT').getStatus()
	stato_milano = getWeather('Milan,IT').getStatus()
	stato_location = getWeather(f'{city},{countrycode}').getStatus()
	attributes = {
		'temp_milano':str(temp_milano)[:4], 
		'temp_roma':str(temp_roma)[:4], 
		'temp_torino':str(temp_torino)[:4],
		'stato_torino':stato_torino,
		'stato_milano':stato_milano,
		'stato_roma':stato_roma,
		'stato_location':stato_location,
		'temp_location':str(temp_location)[:4],
		'location':f'{city},{country}',
		'form':form,
	}


	return render(request, 'main/index.html', attributes)

def city(request):
	if request.method == 'GET':
		form = searchCity(request.GET)
		if form.is_valid():
			city = form.cleaned_data['city']
			tempo = getWeather(city).getTemp()
			stato = getWeather(city).getStatus()
			attributes = {
				'city':city,
				'tempo':tempo,
				'stato':stato,
				'form':form,
			}
			return render(request, 'main/city.html', attributes)
	return redirect('index')





