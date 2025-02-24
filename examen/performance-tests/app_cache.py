from flask import Flask, jsonify
import time
from flask_caching import Cache

app = Flask(__name__)

# Configuration du cache en mémoire 
app.config["CACHE_TYPE"] = "simple"
cache = Cache(app)


def get_user_from_db(user_id):
    time.sleep(2) 
    return {"id": user_id, "name": "User " + str(user_id), "email": "user" + str(user_id) + "@example.com"}

@app.route('/user/<int:user_id>')
@cache.cached(timeout=60, key_prefix="user_")
def get_user(user_id):
    user = get_user_from_db(user_id)
    return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)
