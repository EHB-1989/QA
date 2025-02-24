from flask import Flask, jsonify
from flask_caching import Cache
import time

app = Flask(__name__)


app.config['CACHE_TYPE'] = 'simple' # Here I use simple cache to try to reduce the response time of the /user/<user_id> endpoint
cache = Cache(app)

def get_user_from_db(user_id):
    """Simule le temps de réponse d'une base de données."""
    time.sleep(2)
    return {"id": user_id, "name": "User " + str(user_id), "email": "user" + str(user_id) + "@example.com"}

@app.route('/user/<int:user_id>')
@cache.cached(timeout=3600, key_prefix='user_')
def get_user(user_id):
    user = get_user_from_db(user_id)
    return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)

# With this version of the app, the response time of the /user/<user_id> endpoint is reduced and I got an average response time between 4 and 46 ms. 
# Whereas with the previous version of the app, the average response time was 2000 ms.