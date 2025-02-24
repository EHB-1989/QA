import pytest
import os
import sqlite3
from app import app
from database_manager import init_db, DATABASE_NAME


@pytest.fixture(scope="module")
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture(autouse=True)
def setup_and_teardown():
    if os.path.exists(DATABASE_NAME):
        try:
            os.remove(DATABASE_NAME)
        except PermissionError:
            print(f"Could not remove {DATABASE_NAME}, it might be locked.")

    init_db()
    yield

    try:
        conn = sqlite3.connect(DATABASE_NAME)
        conn.close()
    except Exception as e:
        print(f"Error closing database: {e}")

    if os.path.exists(DATABASE_NAME):
        try:
            os.remove(DATABASE_NAME)
        except PermissionError:
            print(f"Could not remove {DATABASE_NAME} after test.")


def test_ajouter_et_lister_livres(client):
    # Test adding a book
    response = client.post('/ajouter', json={'titre': 'Nouveau Livre', 'auteur': 'Auteur Test'})
    assert response.status_code == 201
    assert response.json == {'message': 'Livre ajouté avec succès'}

    # Test listing books
    response = client.get('/livres')
    assert response.status_code == 200
    livres = response.json
    assert len(livres) >= 1
    assert any(livre.get('titre') == 'Nouveau Livre' for livre in livres)

    # Test adding a book with missing fields
    response = client.post('/ajouter', json={'titre': 'Livre Sans Auteur'})
    assert response.status_code == 400
    assert 'message' in response.json


def test_emprunter_et_retourner_livre(client):
    # Test borrowing a book
    response = client.post('/emprunter', json={'titre': 'Les Misérables'})
    assert response.status_code in [200, 404]

    # Try borrowing again to check if unavailable
    response = client.post('/emprunter', json={'titre': 'Les Misérables'})
    assert response.status_code == 404
    assert response.json == {'message': 'Livre non disponible'}

    # Test returning a book
    response = client.post('/retourner', json={'titre': 'Les Misérables'})
    assert response.status_code in [200, 404]

    # Test borrowing with missing data
    response = client.post('/emprunter', json={})
    assert response.status_code == 400
    assert 'message' in response.json

    # Test returning with missing data
    response = client.post('/retourner', json={})
    assert response.status_code == 400
    assert 'message' in response.json


def test_livre_operations_edge_cases(client):
    # Try borrowing a non-existent book
    response = client.post('/emprunter', json={'titre': 'Livre Inexistant'})
    assert response.status_code == 404
    assert response.json == {'message': 'Livre non disponible'}

    # Try returning a book that hasn't been borrowed
    response = client.post('/retourner', json={'titre': 'Le Petit Prince'})
    assert response.status_code == 404
    assert response.json == {'message': 'Livre non trouvé ou déjà retourné'}


if __name__ == '__main__':
    pytest.main()
