import pytest
from app import app, init_db
from database_manager import get_livres_db

@pytest.fixture
def client():
    """Fixture qui initialise l'application Flask pour les tests."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            init_db()  # Réinitialise la base de données avant chaque test
        yield client
fd
def test_ajouter_livre(client):
    """Test pour ajouter un livre."""
    response = client.post('/ajouter', json={"titre": "Harry Potter", "auteur": "J.K. Rowling"})
    assert response.status_code == 201
    assert response.json['message'] == "Livre ajouté avec succès"

    # Vérifier que le livre est bien dans la base
    livres = get_livres_db()
    assert any(livre["titre"] == "Harry Potter" for livre in livres)

def test_lister_livres(client):
    """Test pour lister les livres."""
    response = client.get('/livres')
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) > 0  # On a bien des livres dans la base

def test_emprunter_livre(client):
    """Test pour emprunter un livre disponible."""
    response = client.post('/emprunter', json={"titre": "1984"})
    assert response.status_code == 200
    assert response.json['message'] == "Livre emprunté avec succès"

    # Vérifier que le livre est maintenant marqué comme emprunté
    livres = get_livres_db()
    for livre in livres:
        if livre["titre"] == "1984":
            assert livre["est_emprunte"] == 1

def test_emprunter_livre_non_disponible(client):
    """Test pour emprunter un livre déjà emprunté."""
    client.post('/emprunter', json={"titre": "1984"})  # Premier emprunt
    response = client.post('/emprunter', json={"titre": "1984"})  # Deuxième emprunt
    assert response.status_code == 404
    assert response.json['message'] == "Livre non disponible"

def test_retourner_livre(client):
    """Test pour retourner un livre emprunté."""
    client.post('/emprunter', json={"titre": "1984"})  # Emprunt
    response = client.post('/retourner', json={"titre": "1984"})
    assert response.status_code == 200
    assert response.json['message'] == "Livre retourné avec succès"

    # Vérifier que le livre est maintenant disponible
    livres = get_livres_db()
    for livre in livres:
        if livre["titre"] == "1984":
            assert livre["est_emprunte"] == 0
