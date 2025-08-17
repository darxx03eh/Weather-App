from django.shortcuts import render
from django.views import View
import requests
from datetime import datetime

# Create your views here.
class WeatherAPIView(View):
    @staticmethod
    def get(request):
        return render(request, 'index.html', {
            'error':'',
            'now':datetime.now()
        })
    def post(self, request):
        city_name = request.POST['city']
        API_KEY = '0c42f7f6b53b244c78a418f4f181282a'
        try:
            url = f'https://api.openweathermap.org./data/2.5/weather?appid={API_KEY}&q={city_name}'
            response = requests.get(url)
            content = response.json()
            city_weather = {
                'city_name': f'{content['name']}, {content['sys']['country']}',
                'date': datetime.now().strftime('%A, %B %d, %Y'),
                'temp': round(content['main']['temp'] - 273.15),
                'description': content['weather'][0]['description'],
                'feels_lik': f'{round(content['main']['feels_like'] - 273.15)}°C',
                'icon': content['weather'][0]['icon'],
                'humidity': f'{round(content['main']['humidity'])}%',
                'wind_speed': f'{content['wind']['speed']} m/s',
                'pressure': f'{content['main']['pressure']} hPa',
                'visibility': f'{content['visibility'] / 1000} Km'
            }
        except Exception as e:
            return render(request, 'index.html', {
                'error':'Please enter the city name correctly.',
                'now':datetime.now()
            })
        return render(request, 'weather.html', city_weather)