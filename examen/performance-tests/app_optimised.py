from flask import Flask, jsonify
from flask_caching import Cache
import time

app = Flask(__name__)

config = {
    "CACHE_TYPE": "simple", 
    "CACHE_DEFAULT_TIMEOUT": 300,  
}
cache = Cache(app)
cache.init_app(app, config=config)

def get_user_from_db(user_id):
    time.sleep(2)  
    return {"id": user_id, "name": "User " + str(user_id), "email": "user" + str(user_id) + "@example.com"}

@app.route('/user/<int:user_id>')
@cache.cached(timeout=300) #on utilise cached parce que la route change en fonction de l'id
def get_user(user_id):
    user = get_user_from_db(user_id)
    return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)
