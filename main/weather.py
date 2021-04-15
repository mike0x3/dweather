from pyowm import OWM



class getWeather:
	def __init__(self, place):
		owm = OWM('46be0e1de12b1aa85fc8bbc4ad75d50f')
		mgr = owm.weather_manager()
		observation = mgr.weather_at_place(place)
		w = observation.weather
		#temperatura in gradi celsius {'temp': 293.4, 'temp_kf': None, 'temp_max': 297.5, 'temp_min': 290.9}
		self.temp = w.temperature('celsius')['temp']
		max_temp = w.temperature('celsius')['temp_max']
		max_temp = w.temperature('celsius')['temp_min']
		self.status = w.status
		#stato ex. sole, nuvole ecc
		#stato = w.get_status() 
		#{'deg': 59, 'speed': 2.660} temperatura e velocita del vento
		#vento = w.get_wind() 
		#percentuale di umidita
		#umidita = w.get_humidity() 

	def getTemp(self):
		return self.temp

	def getStatus(self):
		if self.status == 'Clouds':
			return 'nuvole.png'
		elif self.status == 'Clear':
			return 'sole.png'
		elif self.status == 'Rain':
			return 'pioggia.png'
		elif self.status == 'Snow':
			return 'neve.png'
		else:
			return 'sole-nuvole.png'



		