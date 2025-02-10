import pytest
from flask.testing import FlaskClient

from integration_tests.gestion_app.app import create_app


@pytest.fixture
def client():
    app = create_app(':memory:')  # in memory for testing
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client  # Test runs here
            app.gestionnaire.vider_bd()

def test_creer_utilisateur(client: FlaskClient):
    response = client.post('/utilisateurs', json={'nom': 'John Doe', 'email': 'john@example.com'})
    assert response.status_code == 201
    assert response.json == {"message": "Utilisateur créé avec succès"}

def test_ajouter_tache(client: FlaskClient):
    client.post('/utilisateurs', json={'nom': 'John Doe', 'email': 'john@example.com'})
    response = client.post('/taches', json={'titre': 'Test Tache', 'description': 'Description de la tache', 'utilisateur_email': 'john@example.com'})
    assert response.status_code == 201
    assert response.json == {"message": "Tâche ajoutée avec succès"}

def test_recuperer_taches(client: FlaskClient):
    client.post('/utilisateurs', json={'nom': 'John Doe', 'email': 'john@example.com'})
    client.post('/taches', json={'titre': 'Test Tache', 'description': 'Description de la tache', 'utilisateur_email': 'john@example.com'})
    response = client.get('/taches/john@example.com')
    assert response.status_code == 200
    assert len(response.json) > 0