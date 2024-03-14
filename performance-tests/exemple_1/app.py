from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur l'API de démonstration!"

@app.route('/api/data')
def get_data():
    data = {"key": "value", "number": 42, "message": "Ceci est un test de performance."}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
