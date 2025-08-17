# Weather App 🌤️

[![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/) 
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/) 
[![OpenWeather API](https://img.shields.io/badge/OpenWeatherMap-FF6600?style=for-the-badge&logo=openweathermap&logoColor=white)](https://openweathermap.org/)

---

## Project Overview
**Weather App** is a Django-based web application that allows users to fetch real-time weather information for any city. Users can enter a city name, and the app displays the current temperature, weather description, humidity, wind speed, pressure, visibility, and an appropriate weather icon.

---

## Features
- **Search by City**: Users can enter any city to get weather data.
- **Popular Cities**: Quick links to popular cities like London, Tokyo, New York, etc.
- **Weather Details**:
  - Temperature (°C)
  - Feels Like Temperature
  - Weather Description
  - Humidity (%)
  - Wind Speed (m/s)
  - Pressure (hPa)
  - Visibility (km)
- **Weather Icons**: Dynamic icons change based on day/night (`d`/`n`) or weather conditions.
- **Error Handling**: Displays user-friendly error messages if the city is not found or API fails.

---

## Technologies Used
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **API**: OpenWeatherMap API
- **Templating**: Django Templates (Jinja-like)
- **Static Files**: CSS and JavaScript loaded via `{% static %}`

---

## Setup Instructions

1. **Clone the Repository**
```bash
git clone https://github.com/darxx03eh/Weather-App.git
cd Weather-App
```
2. **Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
3. **Set Up Django**
```bash
python manage.py runserver
```
4. **Open the App**
  - Visit http://127.0.0.1:8000/ in your browser.
  - Enter a city name to get the weather.

---

## Project Structure
```bash
Weather-App/
│
├─ weather/               # Django app
│   ├─ templates/
│   │   ├─ index.html     # Home page (city input)
│   │   └─ weather.html   # Weather result page
│   ├─ static/css/        # CSS files
│   ├─ views.py           # Views (WeatherAPIView)
│   └─ urls.py            # URL routes
├─ manage.py
└─ requirements.txt
```

---

## API Integration
  - Uses OpenWeatherMap API.
  - Fetches data via:
```bash
https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={city_name}
```
  - Converts temperature from Kelvin to Celsius.
  - Parses JSON response to extract weather details.
    
---

## Dynamic Weather Icon
  - The icon code returned by API has d for day and n for night.
    - Example:
      - 02d → Partly cloudy (day)
      - 02n → Partly cloudy (night)
  - Template dynamically loads icon using:
```bash
<img src="https://openweathermap.org/img/w/{{ icon }}.png" alt="weather icon"/>
```

---

## Error Handling
  - If city is not found or API fails:
    - Shows error message on index.html:
      ```bash
      {% if error %}
        <div class="error-message">{{ error }}</div>
      {% endif %}
      ```
  - Backend handles exceptions and API error codes.

---

## Future Improvements
  - Add forecast for multiple days.
  - Add unit conversion (Celsius, Fahrenheit).
  - Implement geolocation support for user's current location.
  - Enhance UI/UX with responsive design and animations.

---

## License
  - This project is open-source and free to use.
