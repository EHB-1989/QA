"""
Version optimisée - Exercice 4 (optionnel)
Eylon Soussan & Kiara

Problème : l'app originale fait un time.sleep(2) à chaque requête,
ce qui donne des temps de réponse > 2000ms détectés par Locust.

Solution : on utilise un cache LRU (functools.lru_cache) pour éviter
d'aller chercher les données en base à chaque fois.
La 1ère requête pour un ID sera lente, mais les suivantes seront instantanées.
"""

from flask import Flask, jsonify
from functools import lru_cache
import time

app = Flask(__name__)


@lru_cache(maxsize=128)
def get_user_from_db(user_id):
    # simule un accès base de données lent
    # grâce au cache LRU, ce délai ne se produit qu'une seule fois par user_id
    time.sleep(2)
    return {
        "id": user_id,
        "name": "User " + str(user_id),
        "email": "user" + str(user_id) + "@example.com"
    }


@app.route('/user/<int:user_id>')
def get_user(user_id):
    # les requêtes répétées pour le même ID sont servies depuis le cache
    user = get_user_from_db(user_id)
    return jsonify(user)


@app.route('/cache/clear', methods=['POST'])
def clear_cache():
    # permet de vider le cache manuellement si besoin
    get_user_from_db.cache_clear()
    return jsonify({"message": "Cache vidé"})


@app.route('/cache/stats', methods=['GET'])
def cache_stats():
    # affiche les statistiques du cache : hits (depuis le cache) et misses (depuis la DB)
    info = get_user_from_db.cache_info()
    return jsonify({
        "hits": info.hits,
        "misses": info.misses,
        "maxsize": info.maxsize,
        "currsize": info.currsize
    })


if __name__ == '__main__':
    app.run(debug=True)
