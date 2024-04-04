#d"apres mes recherche pour amelierer la performance il faut utiliser une mise en cache
from flask import Flask, jsonify
import time

app = Flask(__name__)

cache = {}  

def get_user_from_db(user_id):
    if user_id in cache:
        return cache[user_id]  
    else:
        time.sleep(2) 
        user = {"id": user_id, "name": "User " + str(user_id), "email": "user" + str(user_id) + "@example.com"}
        cache[user_id] = user  
        return user

@app.route('/user/<int:user_id>')
def get_user(user_id):
    user = get_user_from_db(user_id)
    return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)
