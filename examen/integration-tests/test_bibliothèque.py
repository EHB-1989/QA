# tests/test_integration.py

import unittest
import json
import requests
from app import app
from database_manager import init_db, get_livres_db

class TestIntegration(unittest.TestCase):

    def setUp(self):
        # Initialiser la base de données avant chaque test
        init_db()

    def test_ajouter_livre(self):
        livre_number = len(get_livres_db())
        data = {'titre': 'Le Seigneur des Anneaux', 'auteur': 'J.R.R. Tolkien'}
        response = requests.post('http://localhost:5000/ajouter', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['message'], 'Livre ajouté avec succès')

        # Vérifier que le livre a été ajouté à la base de données
        livres = get_livres_db()
        self.assertEqual(len(livres), livre_number+1)
        self.assertEqual(livres[-1]['titre'], 'Le Seigneur des Anneaux')
        self.assertEqual(livres[-1]['auteur'], 'J.R.R. Tolkien')
        self.assertFalse(livres[-1]['est_emprunte'])

def test_emprunter_livre(self):
    # Emprunter un livre disponible
    data = {'titre': 'Le Petit Prince'}
    response = requests.post('http://localhost:5000/emprunter', json=data)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json()['message'], 'Livre emprunté avec succès')

    # Vérifier que le livre a été emprunté dans la base de données
    livres = get_livres_db()
    self.assertTrue(livres[1]['est_emprunte'])

    data = {'titre': 'Le Petit Prince'}
    response = requests.post('http://localhost:5000/retourner', json=data)

    # Emprunter un livre indisponible
    data = {'titre': 'Le Petit Prince'}
    response = requests.post('http://localhost:5000/emprunter', json=data)
    self.assertEqual(response.status_code, 404)
    self.assertEqual(response.json()['message'], 'Livre non disponible')


def test_retourner_livre(self):
        data = {'titre': 'Le Petit Prince'}
        response = requests.post('http://localhost:5000/retourner', json=data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['message'], 'Livre non trouvé ou déjà retourné')

        # Emprunter le livre pour pouvoir le retourner
        response = requests.post('http://localhost:5000/emprunter', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Livre emprunté avec succès')

        # Retourner le livre
        response = requests.post('http://localhost:5000/retourner', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Livre retourné avec succès')

        # Vérifier que le livre a été retourné dans la base de données
        livres = get_livres_db()
        self.assertFalse(livres[1]['est_emprunte'])

if __name__ == '__main__':
    unittest.main()
