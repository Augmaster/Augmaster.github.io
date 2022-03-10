from django.shortcuts import render
import requests
import json

# Create your views here.


def index(request):
    if request.method == 'POST':
        city = request.POST['search']
        api_key = "######"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + api_key + "&q=" + city
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = round(y["temp"] - 273.15, 2)
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            min = round(y["temp_min"] - 273.15, 2)
            max = round(y["temp_max"] - 273.15, 2)
            ressentit = round(y['feels_like'] - 273.15, 2)
            z = x["weather"]
            weather_description = z[0]["description"].capitalize()
            data = {
                'city': city.capitalize(),
                'temp': current_temperature,
                'press': current_pressure,
                'humidity': current_humidity,
                'temp_min': min,
                'temp_max': max,
                'ressentit': ressentit,
                'desc': weather_description
            }
    else:
        data = {}
        return render(request, 'index.html')
    return render(request, 'index.html', data)
