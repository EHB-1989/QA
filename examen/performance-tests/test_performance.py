from flask import Flask, jsonify
from cachelib.simple import SimpleCache
import time

app = Flask(__name__)
cache = SimpleCache()

def get_user_from_db(user_id):
    user = cache.get(str(user_id))  
    if user is None:
        time.sleep(2)  
        user = {"id": user_id, "name": "User " + str(user_id), "email": "user" + str(user_id) + "@example.com"}
        cache.set(str(user_id), user, timeout=300)  
    return user

@app.route('/user/<int:user_id>')
def get_user(user_id):
    user = get_user_from_db(user_id)
    return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)
