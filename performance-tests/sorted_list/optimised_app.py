from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/sort", methods=["POST"])
def sort_numbers():
    data = request.get_json().get("numbers", [])
    sorted_list = sorted(data)
    return jsonify(sorted_list)



