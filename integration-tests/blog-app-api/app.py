from flask import Flask, request, jsonify
from poster import Poster
from database_manager import DBManager

app = Flask(__name__)
db_manager = DBManager("blog.db")  # Nom de la base de données réelle pour l'exemple


@app.route("/posts", methods=["POST"])
def create_post():
    data = request.json
    post = Poster(data["title"], data["content"])
    db_manager.add_post(post)
    return jsonify({"message": "Post added successfully"}), 201


@app.route("/posts", methods=["GET"])
def get_posts():
    posts = db_manager.get_posts()
    return jsonify([{"title": post.title, "content": post.content} for post in posts])


if __name__ == "__main__":
    app.run(debug=True)
