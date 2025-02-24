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

from flask import Flask, jsonify
from flask_caching import Cache
import time

app = Flask(__name__)
app.config["CACHE_TYPE"] = "simple"
cache = Cache(app)

def get_user_from_db(user_id):
    time.sleep(2)  # Simule le temps de réponse de la base de données
    user = {
        "id": user_id,
        "name": "User " + str(user_id),
        "email": "user" + str(user_id) + "@example.com",
    }
    return user


@app.route("/user/<int:user_id>")
@cache.cached(timeout=3600, key_prefix="user_id_")
def get_user(user_id):
    user = get_user_from_db(user_id)
    return jsonify(user)

if __name__ == "__main__":
    app.run(debug=True)
