from flask import Flask, jsonify, request
from flask_caching import Cache
import time

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
cache = Cache(app)

@cache.memorize(timeout=60)
def get_weather_data(city):
    time.sleep(2)
    return {
        "city":city,
        "temperature": "20°C",
        "description":"Ensoleillé"
    }


@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city', 'Paris')
    weather_data = get_weather_data(city)
    return jsonify(weather_data)


if __name__ == '__main__':
    app.run(debug=True)