from flask import Flask, jsonify
from functools import lru_cache

app = Flask(__name__)


@lru_cache(maxsize=128)
def get_user_from_db(user_id):
    return {"id": user_id, "name": "User " + str(user_id), "email": "user" + str(user_id) + "@example.com"}


@app.route('/user/<int:user_id>')
def get_user(user_id):
    user = get_user_from_db(user_id)
    return jsonify(user)


if __name__ == '__main__':
    app.run(debug=True)
