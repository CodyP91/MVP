from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Weather API key (replace 'YOUR_API_KEY' with your actual API key)
API_KEY = 'YOUR_API_KEY'
WEATHER_API_URL = 'https://api.openweathermap.org/data/2.5/weather'

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    
    try:
        response = requests.get(WEATHER_API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        weather_data = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
        return jsonify(weather_data)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'Failed to fetch weather data'}), 500

if __name__ == '__main__':
    app.run()
