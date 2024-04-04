# tests/test_integration.py

import unittest
import json
import requests
from app import app
from database_manager import init_db, get_livres_db

class TestIntegration(unittest.TestCase):

    def setUp(self):
        init_db()

    def test_ajouter_livre(self):
        livre_number = len(get_livres_db())
        data = {'titre': 'Le Seigneur des Anneaux', 'auteur': 'J.R.R. Tolkien'}
        response = requests.post('http://localhost:5000/ajouter', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['message'], 'Livre ajouté avec succès')

        livres = get_livres_db()
        self.assertEqual(len(livres), livre_number+1)
        self.assertEqual(livres[-1]['titre'], 'Le Seigneur des Anneaux')
        self.assertEqual(livres[-1]['auteur'], 'J.R.R. Tolkien')
        self.assertFalse(livres[-1]['est_emprunte'])

def test_emprunter_livre(self):
    
    data = {'titre': 'Le Petit Prince'}
    response = requests.post('http://localhost:5000/emprunter', json=data)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json()['message'], 'Livre emprunté avec succès')

    livres = get_livres_db()
    self.assertTrue(livres[1]['est_emprunte'])

    data = {'titre': 'Le Petit Prince'}
    response = requests.post('http://localhost:5000/retourner', json=data)

    data = {'titre': 'Le Petit Prince'}
    response = requests.post('http://localhost:5000/emprunter', json=data)
    self.assertEqual(response.status_code, 404)
    self.assertEqual(response.json()['message'], 'Livre non disponible')


def test_retourner_livre(self):
    
        data = {'titre': 'Le Petit Prince'}
        response = requests.post('http://localhost:5000/retourner', json=data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['message'], 'Livre non trouvé ou déjà retourné')

        response = requests.post('http://localhost:5000/emprunter', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Livre emprunté avec succès')

        response = requests.post('http://localhost:5000/retourner', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Livre retourné avec succès')

        livres = get_livres_db()
        self.assertFalse(livres[1]['est_emprunte'])

if __name__ == '__main__':
    unittest.main()
