from flask import Flask, jsonify, request
from flask_caching import Cache
import time  # Simule un délai d'accès à une API externe

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

def get_weather_data(city):
    """Simule la récupération de données météorologiques depuis une API externe avec un délai."""
    time.sleep(2)  # Simule un délai de 2 secondes pour la récupération des données
    return {
        "city": city,
        "temperature": "20°C",
        "description": "Ensoleillé"
    }

@app.route('/weather', methods=['GET'])
@cache.cached(timeout=60)
def weather():
    city = request.args.get('city', 'Paris')
    weather_data = get_weather_data(city)
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)
