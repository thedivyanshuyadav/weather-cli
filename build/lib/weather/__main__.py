import sys
import requests
import argparse
import json
 
def weatherInfo(city):
	try:
		print('\t\tWeather Information for city:',city)
		choiceScreen ="""
			Choose Options
			1. Humidity
			2. Pressure
			3. Average temperature
			4. Wind Speed
			5. Wind degree
			6. UV Index
			7. Another City Weather
			8. Exit
			Choice: """
		api_key = '53735fde8bca0a7d86d184790bb52530'
			
		url =  f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}"
		data = requests.get(url).json()
		lat = data['coord']['lat']
		lon = data['coord']['lon']
		dt = data['dt']
		
		url = f"http://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={dt}&appid={api_key}"
		data = requests.get(url).json()['current']
		
		while True:
			ch = int(input(choiceScreen))
			if ch==8: break
			if ch!=7:print('\n\t\tResult:',end='')
			if ch==1: print('Humidity:',data['humidity'],'%')
			elif ch==2: print('Pressure:',data['pressure'],'hPa')
			elif ch==3:print('Average Temperature:',data['temp'],'Kelvin') 
			elif ch==4:print('Wind Speed:',data['wind_speed'],'meter/sec')
			elif ch==5:print('Wind Degree:',data['wind_deg'])
			elif ch==6:print('UV Index',data['uvi'])
			elif ch==7:
				city  = str(input('\n\t\tEnter new city: '))
				url =  f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}"
				data = requests.get(url).json()
				lat = data['coord']['lat']
				lon = data['coord']['lon']
				dt = data['dt']
				url = f"http://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={dt}&appid={api_key}"
				data = requests.get(url).json()['current']
	except:print("Something went wrong!")		

if __name__ =='__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('weather', nargs=1,metavar=('city'),type=str, default=1.0,help="weather information for given city.")
	args = parser.parse_args()
	if type(args.weather)==list:
		weatherInfo(args.weather[0])
	else:
		print("Something went wrong!")
	
		