"""
------------------------------------------------------------
 Nom du fichier : optimized_app_hugo.py
 Auteur        : Moulard Hugo
 Date          : 24/02/2025
 Description   : Application optimizé avec de la mise en cache
------------------------------------------------------------
"""

from flask import Flask, jsonify
import time
from flask_caching import Cache


app = Flask(__name__)

#Mise en place d'un cache pour être encore plus opti

# Configuration du cache
app.config["CACHE_TYPE"] = "simple"
cache = Cache(app)

# Simulation d'une base de données lente
def get_user_from_db(user_id):
    time.sleep(2)  # Simule un délai réseau
    return {"id": user_id, "name": "User " + str(user_id), "email": "user" + str(user_id) + "@example.com"}

@app.route('/user/<int:user_id>')
@cache.cached(timeout=60, key_prefix="user_")  # Mise en cache pour 60s
def get_user(user_id):
    return jsonify(get_user_from_db(user_id))

if __name__ == '__main__':
    app.run(debug=True)
