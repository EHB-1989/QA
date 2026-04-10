from flask import Flask, jsonify
import time

app = Flask(_name_)

# Simulation d'un cache en mémoire
cache = {}

def get_user_from_db(user_id):
    # On simule toujours la lenteur de la DB
    time.sleep(2)
    return {"id": user_id, "name": "User " + str(user_id), "email": f"user{user_id}@example.com"}

@app.route('/user/<int:user_id>')
def get_user(user_id):
    # 1. On vérifie si l'utilisateur est déjà dans le cache
    if user_id in cache:
        return jsonify(cache[user_id])
    
    # 2. Sinon, on va le chercher (très lentement)
    user = get_user_from_db(user_id)
    
    # 3. On l'enregistre dans le cache pour la prochaine fois
    cache[user_id] = user
    
    return jsonify(user)

if _name_ == '_main_':
    app.run(debug=False)