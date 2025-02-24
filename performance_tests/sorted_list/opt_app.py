from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sort', methods=['POST'])
def sort_numbers():
    list = request.get_json().get('numbers', [])
    sorted_list = sorted(list)     
    return jsonify(sorted_list)

if __name__ == '__main__':
    app.run(debug=True)
