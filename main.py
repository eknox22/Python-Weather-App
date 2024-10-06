import requests
from rich import print
from datetime import datetime

def display_current_weather(city):
    api_key = "t61a3de96178c340b47o7ff32962bb7f"
    api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}"

    response = requests.get(api_url)
    current_weather_data = response.json()
    current_weather_city = current_weather_data['city']
    current_weather_temperature = current_weather_data['temperature']['current']

    print(f"The temperature in {current_weather_city} is {round(current_weather_temperature)}ºC")

def display_forecast_weather(city_name):
    api_key = "t61a3de96178c340b47o7ff32962bb7f"
    api_url = f"https://api.shecodes.io/weather/v1/forecast?query={city_name}&key={api_key}"

    response = requests.get(api_url)
    forecast_weather_data = response.json()

    for day in forecast_weather_data['daily']:
        timestamp = day['time']

        date = datetime.fromtimestamp(timestamp)
        formatted_day = date.strftime("%A")
        temperature = day['temperature']['day']
        print(f"{formatted_day}: {round(temperature)}ºC")


city_name = input('Enter a city: ')
city_name = city_name.strip()

if city_name:
    display_current_weather(city_name)
    display_forecast_weather(city_name)
else:
    print('Please try again with a city.')