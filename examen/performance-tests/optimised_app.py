from flask import Flask, jsonify
from functools import lru_cache
import time

app = Flask(__name__)


@lru_cache(maxsize=128)
def get_user_from_db(user_id):
    time.sleep(0.2)
    return {
        "id": user_id,
        "name": f"User {user_id}",
        "email": f"user{user_id}@example.com",
    }


@app.route('/user/<int:user_id>')
def get_user(user_id):
    user = get_user_from_db(user_id)
    return jsonify(user)


if __name__ == '__main__':
    app.run(debug=True)
