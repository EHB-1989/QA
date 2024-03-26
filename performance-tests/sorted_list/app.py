from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sort', methods=['POST'])
def sort_numbers():
    data = request.get_json().get('numbers', [])
    sorted_list = []
    for number in data:
        sorted_list.append(number)
        sorted_list = sorted(sorted_list)
    return jsonify(sorted_list)

if __name__ == '__main__':
    app.run(debug=True)
