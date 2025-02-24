#!/usr/bin/env python3
# -*-coding:utf-8 -*-
'''
@File    :   optimised_app.py
@Time    :   2025/02/24
@Author  :   FOURMONT Baptiste
@Version :   1.0
@Contact :   baptiste_fourmont@tutanota.com
@Desc    :   None
'''

from flask import Flask, jsonify, request
from flask_caching import Cache
import time

app = Flask(__name__)
cache = Cache(app)

def get_user_from_db(user_id):
    user = {
        "id": user_id,
        "name": "User " + str(user_id),
        "email": "user" + str(user_id) + "@example.com",
    }
    return user


@app.route("/user/<int:user_id>")
def get_user(user_id):
    user = cache.get(str(user_id))
    if user is None:
        user = get_user_from_db(user_id)
        cache.set(str(user_id), user, timeout=3600)
    return jsonify(user)


if __name__ == "__main__":
    app.run(debug=True)
