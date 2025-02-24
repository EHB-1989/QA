import pytest
from flask import Flask
from app import app  # Assure-toi que ton fichier Flask s'appelle app.py

@pytest.fixture
def client():
    """Crée un client de test pour Flask."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_create_post(client):
    """Test la route POST /posts"""
    response = client.post("/posts", json={"title": "Hello", "content": "World"})
    assert response.status_code == 201, "Le POST /posts devrait retourner un code 201"
    assert response.get_json()["message"] == "Post added successfully"

def test_get_posts(client):
    """Test la route GET /posts"""
    response = client.get("/posts")
    assert response.status_code == 200, "Le GET /posts devrait retourner un code 200"
    data = response.get_json()
    assert isinstance(data, list), "La réponse doit être une liste"
    assert len(data) > 0, "Il devrait y avoir au moins un post enregistré"
