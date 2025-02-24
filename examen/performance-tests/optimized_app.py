from flask import Flask, jsonify
import time

app = Flask(__name__)

# ajout du cache pour optimiser
app.config['CACHE_TYPE'] = 'simple'
cache = Cache(app)

# Simulation d'une base de données avec un délai
async def get_user_from_db(user_id):
    await asyncio.sleep(2)  
    return {"id": user_id, "name": "User " + str(user_id), "email": "user" + str(user_id) + "@example.com"}

@app.route('/user/<int:user_id>')
async def get_user(user_id):
    user = await get_user_from_db(user_id) 
    return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)