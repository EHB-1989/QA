import json
from app import *
import pytest

def test_create_post(client):
   
    post_data = {"title": "Test Title", "content": "Test Content"}

    response = client.post('/posts', json=post_data)

    assert response.status_code == 201

    data = response.get_json()
    assert data["message"] == "Post added successfully"

def test_get_posts(client):
   
    response = client.get('/posts')

    assert response.status_code == 200

    data = response.get_json()
    assert isinstance(data, list)  

    assert len(data) >= 0 
    if len(data) > 0:
        assert all("title" in post and "content" in post for post in data)


if __name__ == "__main__":
    
    pytest.main()
