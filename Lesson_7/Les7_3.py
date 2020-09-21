from time import strftime
import requests
from pprint import pprint
from datetime import datetime

now = datetime.now()
city_name = input('Enter the city name: ')
API_ID = 'f9ada9efec6a3934dad5f30068fdcbb8'

weather_request = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?q=city&cnt=5&units=metric&appid',
                               params={'q': city_name, 'units': 'metric', 'cnt': 5, 'lang': 'ru', 'appid': API_ID})
weather_data = weather_request.json()
pprint(weather_data['list'][0]['temp'])

with open('20-09-2020-Odessa-5-days-weather-forecast.txt', 'w+', encoding="utf-8") as file_object:
    weather_data = file_object.write(strftime("%d-%m-%Y"))
pprint(weather_data)
