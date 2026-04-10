from flask import Flask, jsonify
from concurrent.futures import ThreadPoolExecutor
import time

app = Flask(__name__)

# Cache en mémoire pour éviter les appels répétés à la base de données
cache = {}

# Pool de threads pour traiter les appels BDD en parallèle
executor = ThreadPoolExecutor(max_workers=20)

def get_user_from_db(user_id):
    time.sleep(2)  # Simule le temps de réponse de la base de données
    return {"id": user_id, "name": "User " + str(user_id), "email": "user" + str(user_id) + "@example.com"}

@app.route('/user/<int:user_id>')
def get_user(user_id):
    # Si déjà en cache, réponse instantanée
    if user_id in cache:
        return jsonify(cache[user_id])

    # Sinon, on soumet l'appel BDD au pool de threads (non bloquant)
    future = executor.submit(get_user_from_db, user_id)
    user = future.result()
    cache[user_id] = user
    return jsonify(user)

if __name__ == '__main__':
    # threaded=True + pool de threads = traitement massivement parallèle
    app.run(debug=True, threaded=True)
