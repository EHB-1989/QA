from flask import Flask, request, jsonify
from poster import Poster
from database_manager import DBManager
import pytest
import os

app = Flask(__name__)
db_manager = DBManager('blog.db')  # Nom de la base de données réelle pour l'exemple

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.json
    post = Poster(data['title'], data['content'])
    db_manager.add_post(post)
    return jsonify({"message": "Post added successfully"}), 201

@app.route('/posts', methods=['GET'])
def get_posts():
    posts = db_manager.get_posts()
    return jsonify([{"title": post.title, "content": post.content} for post in posts])

if __name__ == '__main__':
    app.run(debug=True)

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            if os.path.exists('blog.db'):
                del db_manager
                os.remove('blog.db')
                db_manager = DBManager('blog.db')
        yield client

def test_create_post(client):
    response = client.post('/posts', json={"title": "title", "content": "content"})
    assert response.status_code == 201
    assert response.json == {"message": "Post added successfully"}

def test_get_posts(client):
    client.post('/posts', json={"title": "title", "content": "content"})  
    response = client.get('/posts')
    assert response.status_code == 200
    assert response.json == [{"title": "title", "content": "content"}]

