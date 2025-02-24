from Scripts.pywin32_testall import this_dir
from flask import Flask, request, jsonify
from waitress import serve

app = Flask(__name__)

@app.route('/sort', methods=['POST'])
def sort_numbers():
    data = request.get_json().get('numbers', [])
    sorted_list = sorted(data)
    return jsonify(sorted_list)


if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000, threads=32)