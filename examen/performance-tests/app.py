from flask import Flask, jsonify
from flask_caching import Cache
import time

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache', 'CACHE_DEFAULT_TIMEOUT': 60})

# Simulation d'une base de données avec un délai
def get_user_from_db(user_id):
    time.sleep(2)  # Simule le temps de réponse de la base de données
    return {"id": user_id, "name": "User " + str(user_id), "email": "user" + str(user_id) + "@example.com"}

@app.route('/user/<int:user_id>')
@cache.cached()
def get_user(user_id):
    user = get_user_from_db(user_id)
    return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)
