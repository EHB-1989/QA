"""
------------------------------------------------------------
 Nom du fichier : integration_test_hugo.py
 Auteur        : Moulard Hugo
 Date          : 24/02/2025
 Description   : Test d'intégration de l'API pour Bibliotheque et Livre
------------------------------------------------------------
"""

import pytest
from app import app, init_db, get_db_connection

def setup_module(module):
    """Réinitialise la base de données avant chaque test."""
    init_db()

def test_ajouter_livre():
    client = app.test_client()
    response = client.post('/ajouter', json={
        'titre': 'Test Livre',
        'auteur': 'Auteur Test'
    })
    assert response.status_code == 201
    assert response.json['message'] == 'Livre ajouté avec succès'

def test_lister_livres():
    client = app.test_client()
    response = client.get('/livres')
    assert response.status_code == 200
    livres = response.json
    assert any(livre['titre'] == 'Test Livre' for livre in livres)

def test_emprunter_livre():
    client = app.test_client()
    response = client.post('/emprunter', json={'titre': 'Test Livre'})
    assert response.status_code == 200
    assert response.json['message'] == 'Livre emprunté avec succès'
    
    # Vérifier que le livre est bien marqué comme emprunté
    with get_db_connection() as conn:
        livre = conn.execute("SELECT * FROM livres WHERE titre = ?", ('Test Livre',)).fetchone()
        assert livre['est_emprunte'] == 1

def test_emprunter_livre_non_disponible():
    client = app.test_client()
    response = client.post('/emprunter', json={'titre': 'Test Livre'})
    assert response.status_code == 404
    assert response.json['message'] == 'Livre non disponible'

def test_retourner_livre():
    client = app.test_client()
    response = client.post('/retourner', json={'titre': 'Test Livre'})
    assert response.status_code == 200
    assert response.json['message'] == 'Livre retourné avec succès'
    
    # Vérifier que le livre est bien marqué comme disponible
    with get_db_connection() as conn:
        livre = conn.execute("SELECT * FROM livres WHERE titre = ?", ('Test Livre',)).fetchone()
        assert livre['est_emprunte'] == 0

def test_retourner_livre_non_emprunte():
    client = app.test_client()
    response = client.post('/retourner', json={'titre': 'Test Livre'})
    assert response.status_code == 404
    assert response.json['message'] == 'Livre non trouvé ou déjà retourné'
