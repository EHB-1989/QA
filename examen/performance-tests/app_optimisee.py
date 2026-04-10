from flask import Flask, jsonify
from functools import lru_cache
import time

app = Flask(__name__)

@lru_cache(maxsize=128)          # Cache en mémoire
def get_user_from_db(user_id):
    time.sleep(2)   
    return (user_id, "User " + str(user_id), "user" + str(user_id) + "@example.com")

@app.route('/user/<int:user_id>')
def get_user(user_id):
    uid, name, email = get_user_from_db(user_id)
    return jsonify({"id": uid, "name": name, "email": email})

if __name__ == '__main__':
    app.run(debug=True)     