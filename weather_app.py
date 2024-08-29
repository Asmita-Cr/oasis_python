import requests
import json

api_key= '0f40ec74ea27598e08e05e48b2a39234'

baseURL= "https://api.openweathermap.org/data/2.5/weather?q="

city_name= input ("Enter your city: ")
print(("The temmperatures are in farenheit:"))

completeURL = baseURL + city_name + "&appid=" + api_key
response = requests.get(completeURL)

data = response. json()

print("Current Temperature", data["main"]["temp"])
print("Current Temperature Feels Like", data["main"]["feels_like"])
print("Maximum Temperature", data["main"]["temp_max"])
print("Minimum Temperature", data["main"]["temp_min"])
print("Humidity", data["main"]["humidity"])

