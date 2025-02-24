
@app.route('/sort', methods=['POST'])
def sort_numbers():
    data = request.get_json().get('numbers', [])
    return jsonify(sorted(data))
