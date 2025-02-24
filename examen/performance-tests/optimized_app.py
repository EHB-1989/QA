from flask import Flask, jsonify
from flask_caching import Cache
import time

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'  # Use a simple in-memory cache
cache = Cache(app)

# Simulation of a database with a delay
@cache.memoize(timeout=60)  # Cache the result for 60 seconds
def get_user_from_db(user_id):
    time.sleep(2)  # Simulate database response time
    return {"id": user_id, "name": "User " + str(user_id), "email": "user" + str(user_id) + "@example.com"}

@app.route('/user/<int:user_id>')
def get_user(user_id):
    user = get_user_from_db(user_id)
    return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)
