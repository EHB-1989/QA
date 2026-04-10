from flask import Flask, jsonify
from flask_caching import Cache
import time

app = Flask(__name__)

app.config["CACHE_TYPE"] = "SimpleCache"
app.config["CACHE_DEFAULT_TIMEOUT"] = 60

cache = Cache(app)


@cache.memoize(timeout=60)
def recuperer_utilisateur_depuis_db(user_id: int) -> dict:
    time.sleep(2)
    return {
        "id": user_id,
        "name": f"User {user_id}",
        "email": f"user{user_id}@example.com"
    }


@app.route('/user/<int:user_id>')
def obtenir_utilisateur(user_id: int):
    donnees_utilisateur = recuperer_utilisateur_depuis_db(user_id)
    return jsonify(donnees_utilisateur)


@app.route('/cache/clear', methods=['POST'])
def vider_cache():
    cache.clear()
    return jsonify({"message": "Cache vidé avec succès"}), 200


if __name__ == '__main__':
    app.run(debug=True)