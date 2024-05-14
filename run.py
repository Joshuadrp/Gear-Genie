import requests

api_key = '6a3f2cc91e7c4aa8d6506c5f08f260e4'

user_location = input('Please state the place you want to go:\n')

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_location}&units=metric&APPID={api_key}")

weather = weather_data.json()['weather'][0]['main']
temp = weather_data.json()['main']['temp']

# print(weather_data.json())


