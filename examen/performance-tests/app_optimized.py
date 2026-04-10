from flask import Flask, jsonify
import time
from functools import lru_cache

app = Flask(__name__)

# Simulation d'une base de données avec un délai
# L'optimisation principale ici est l'ajout d'un cache LRU (Least Recently Used)
# Les appels répétés pour le même user_id retourneront le résultat instanément
@lru_cache(maxsize=100)
def get_user_from_db(user_id):
    time.sleep(2)  # Simule la lenteur de la requête initiale de la base de données
    return {"id": user_id, "name": "User " + str(user_id), "email": "user" + str(user_id) + "@example.com"}

@app.route('/user/<int:user_id>')
def get_user(user_id):
    user = get_user_from_db(user_id)
    return jsonify(user)

if __name__ == '__main__':
    # Dans un cas réel de production, on utiliserait Memcached ou Redis
    app.run(debug=True)
