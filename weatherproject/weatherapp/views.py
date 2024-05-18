import urllib.request
import json
from django.shortcuts import render
from django.conf import settings


def index(request):
    api_key = settings.API_KEY
    print(api_key)
    if request.method == "POST":
        city = request.POST["city"]
        source = urllib.request.urlopen(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
        ).read()
        data_list = json.loads(source)

        data = {
            "city": city,
            "temp": str(round((data_list["main"]["temp"]))) + "°C",
            "pressure": str(data_list["main"]["pressure"]) + "Pa",
            "humidity": str(data_list["main"]["humidity"]) + "%",
            "main": str(data_list["main"]),
            "icon": str(data_list["weather"][0]["icon"]),
            "description": str(data_list["weather"][0]["description"]),
        }
    else:
        data = {}

    print(data)
    return render(request, "main/index.html", data)
