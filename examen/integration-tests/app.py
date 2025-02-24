# app.py
from flask import Flask, request, jsonify
from database_manager import init_db, ajouter_livre_db, get_livres_db, emprunter_livre_db, retourner_livre_db, get_db_connection
import pytest
import os

app = Flask(__name__)

@app.route('/ajouter', methods=['POST'])
def ajouter_livre():
    data = request.json
    ajouter_livre_db(data['titre'], data['auteur'])
    return jsonify({'message': 'Livre ajouté avec succès'}), 201

@app.route('/livres', methods=['GET'])
def lister_livres():
    livres = get_livres_db()
    return jsonify([dict(livre) for livre in livres])


@app.route('/emprunter', methods=['POST'])
def emprunter_livre():
    titre = request.json['titre']
    if emprunter_livre_db(titre):
        return jsonify({'message': 'Livre emprunté avec succès'}), 200
    else:
        return jsonify({'message': 'Livre non disponible'}), 404

@app.route('/retourner', methods=['POST'])
def retourner_livre():
    titre = request.json['titre']
    if retourner_livre_db(titre):
        return jsonify({'message': 'Livre retourné avec succès'}), 200
    else:
        return jsonify({'message': 'Livre non trouvé ou déjà retourné'}), 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
    
@pytest.fixture
def client():
    with app.test_client() as client:
        # supprime le contenu de la base de données avant chaque test
        with get_db_connection() as conn:
            conn.execute('DELETE FROM livres')
        yield client

def test_ajouter_livre(client):
    response = client.post('/ajouter', json={'titre': 'Le Seigneur des Anneaux', 'auteur': 'J.R.R. Tolkien'})
    assert response.status_code == 201
    assert response.json == {'message': 'Livre ajouté avec succès'}

def test_lister_livres(client):
    response = client.get('/livres')
    assert response.status_code == 200
    assert len(response.json) == 0
    client.post('/ajouter', json={'titre': 'Le Seigneur des Anneaux', 'auteur': 'J.R.R. Tolkien'})
    response = client.get('/livres')
    assert len(response.json) == 1
    assert response.json[0]['titre'] == 'Le Seigneur des Anneaux'

def test_emprunter_livre(client):
    # emprunter un livre inexistant
    response = client.post('/emprunter', json={'titre': 'Le Seigneur des Anneaux'})
    assert response.status_code == 404
    assert response.json == {'message': 'Livre non disponible'}
    
    client.post('/ajouter', json={'titre': 'Le Seigneur des Anneaux', 'auteur': 'J.R.R. Tolkien'})
    
    response = client.post('/emprunter', json={'titre': 'Le Seigneur des Anneaux'})
    assert response.status_code == 200
    assert response.json == {'message': 'Livre emprunté avec succès'}
    
    # emprunter un livre déjà emprunté
    response = client.post('/emprunter', json={'titre': 'Le Seigneur des Anneaux'})
    assert response.status_code == 404
    assert response.json == {'message': 'Livre non disponible'}


def test_retourner_livre(client):
    #retourner un livre inexistant
    response = client.post('/retourner', json={'titre': 'Livre Inexistant'})
    assert response.status_code == 404
    assert response.json == {'message': 'Livre non trouvé ou déjà retourné'}
    
    #retourner un livre non emprunté
    client.post('/ajouter', json={'titre': 'Le Seigneur des Anneaux', 'auteur': 'J.R.R. Tolkien'})
    response = client.post('/retourner', json={'titre': 'Le Seigneur des Anneaux'})
    assert response.status_code == 404
    assert response.json == {'message': 'Livre non trouvé ou déjà retourné'}
    
    #retourner un livre emprunté
    client.post('/emprunter', json={'titre': 'Le Seigneur des Anneaux'})
    response = client.post('/retourner', json={'titre': 'Le Seigneur des Anneaux'})
    assert response.status_code == 200
    assert response.json == {'message': 'Livre retourné avec succès'}
    
    #retourner un livre déjà retourné
    response = client.post('/retourner', json={'titre': 'Le Seigneur des Anneaux'})
    assert response.status_code == 404
    assert response.json == {'message': 'Livre non trouvé ou déjà retourné'}
    

