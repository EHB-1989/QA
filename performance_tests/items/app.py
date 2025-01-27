from flask import Flask, jsonify, request
from item import Item
from database_manager import DBManager
from flask_sqlalchemy import SQLAlchemy
import time

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# db = SQLAlchemy(app)

app = Flask(__name__)
db_manager = DBManager('items.db')  # Nom de la base de données réelle pour l'exemple


@app.route('/')
def home():
    return "Bienvenue sur l'API de démonstration!"

@app.route('/api/data')
def get_data():
    data = {"key": "value", "number": 42, "message": "Ceci est un test de performance."}
    return jsonify(data)

@app.route('/api/items', methods=['POST'])
def create_item():
    data = request.get_json()
    item = Item(data['name'], data['description'])
    db_manager.add_item(item)
    return jsonify({"message": "Item créé avec succès!"}), 201

@app.route('/api/simulate_long_processing')
def simulate_long_processing():
    time.sleep(5)  # Simule un traitement long de 5 secondes
    return jsonify({"message": "Traitement long terminé!"})

if __name__ == '__main__':
    app.run(debug=True)
   
