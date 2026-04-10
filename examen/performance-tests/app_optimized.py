from flask import Flask, jsonify
import time

app = Flask(__name__)

_USER_CACHE = {}


def get_user_from_db(user_id):
    if user_id in _USER_CACHE:
        return _USER_CACHE[user_id]

    time.sleep(2)
    user = {
        "id": user_id,
        "name": "User " + str(user_id),
        "email": "user" + str(user_id) + "@example.com",
    }
    _USER_CACHE[user_id] = user
    return user


@app.route("/user/<int:user_id>")
def get_user(user_id):
    user = get_user_from_db(user_id)
    return jsonify(user)


if __name__ == "__main__":
    app.run(debug=True)
