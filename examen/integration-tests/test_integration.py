import unittest
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import database_manager
from app import app
from database_manager import init_db

TEST_DB = "test_bibliotheque.db"


class TestIntegrationBibliotheque(unittest.TestCase):

    def setUp(self):
        # j'utilise une base de données de test séparée
        database_manager.DATABASE_NAME = TEST_DB

        app.config['TESTING'] = True
        self.client = app.test_client()

        # j'initialise la base de données de test
        init_db()

    def tearDown(self):
        # et je supprime la base de données de test après chaque test
        if os.path.exists(TEST_DB):
            os.remove(TEST_DB)

    # --- Tests route /ajouter ---

    def test_ajouter_livre(self):
        response = self.client.post('/ajouter', json={
            'titre': 'Don Quichotte',
            'auteur': 'Cervantes'
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['message'], 'Livre ajouté avec succès')

    # --- Tests route /livres ---

    def test_lister_livres(self):
        response = self.client.get('/livres')
        self.assertEqual(response.status_code, 200)
        livres = response.get_json()
        self.assertIsInstance(livres, list)
        self.assertEqual(len(livres), 3)  

    def test_lister_livres_apres_ajout(self):
        self.client.post('/ajouter', json={'titre': 'Dune', 'auteur': 'Frank Herbert'})
        response = self.client.get('/livres')
        livres = response.get_json()
        self.assertEqual(len(livres), 4)

    # --- Tests route /emprunter ---

    def test_emprunter_livre_disponible(self):
        response = self.client.post('/emprunter', json={'titre': 'Les Misérables'})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['message'], 'Livre emprunté avec succès')

    def test_emprunter_livre_inexistant(self):
        response = self.client.post('/emprunter', json={'titre': 'Livre Inconnu'})
        self.assertEqual(response.status_code, 404)

    def test_emprunter_livre_deja_emprunte(self):
        self.client.post('/emprunter', json={'titre': 'Les Misérables'})
        response = self.client.post('/emprunter', json={'titre': 'Les Misérables'})
        self.assertEqual(response.status_code, 404)

    # --- Tests route /retourner ---

    def test_retourner_livre_emprunte(self):
        self.client.post('/emprunter', json={'titre': '1984'})
        response = self.client.post('/retourner', json={'titre': '1984'})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['message'], 'Livre retourné avec succès')

    def test_retourner_livre_non_emprunte(self):
        response = self.client.post('/retourner', json={'titre': '1984'})
        self.assertEqual(response.status_code, 404)

    def test_retourner_livre_inexistant(self):
        response = self.client.post('/retourner', json={'titre': 'Livre Inconnu'})
        self.assertEqual(response.status_code, 404)



    # --- Test flux complet ---

    def test_flux_complet(self):
        # Ajout
        self.client.post('/ajouter', json={'titre': 'Dune', 'auteur': 'Frank Herbert'})
        # Emprunt
        response = self.client.post('/emprunter', json={'titre': 'Dune'})
        self.assertEqual(response.status_code, 200)
        # Retour
        response = self.client.post('/retourner', json={'titre': 'Dune'})
        self.assertEqual(response.status_code, 200)
        # Disponible à nouveau
        response = self.client.post('/emprunter', json={'titre': 'Dune'})
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()