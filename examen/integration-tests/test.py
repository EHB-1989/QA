import unittest
import os
import sqlite3
from app import app
from database_manager import init_db, DATABASE_NAME

class TestBibliothequeAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        cls.client = app.test_client()

    def setUp(self):
        if os.path.exists(DATABASE_NAME):
            try:
                os.remove(DATABASE_NAME)
            except PermissionError:
                print(f"Could not remove {DATABASE_NAME}, it might be locked.")

        init_db()

    def tearDown(self):
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

    def test_ajouter_et_lister_livres(self):
        # Test ajouter livre
        response = self.client.post('/ajouter', json={'titre': 'Hello', 'auteur': 'Jarod'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {'message': 'Livre ajouté avec succès'})

        # Test lister livres
        response = self.client.get('/livres')
        self.assertEqual(response.status_code, 200)
        livres = response.json
        self.assertGreaterEqual(len(livres), 1)
        self.assertTrue(any(livre.get('titre') == 'Hello' for livre in livres))


    def test_emprunter_et_retourner_livre(self):
        # Test emprunter
        response = self.client.post('/emprunter', json={'titre': 'Le Petit Prince'})
        self.assertIn(response.status_code, [200])

        # Test emprunter un livre deja emprunte 
        response = self.client.post('/emprunter', json={'titre': 'Le Petit Prince'})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {'message': 'Livre non disponible'})

        # Test emprunte un livre inexistant
        response = self.client.post('/emprunter', json={'titre': 'Livre Inexistant'})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {'message': 'Livre non disponible'})

        # Test retourner un livre
        response = self.client.post('/retourner', json={'titre': 'Le Petit Prince'})
        self.assertIn(response.status_code, [200])

        # Test retounrer un livre deja retourne
        response = self.client.post('/retourner', json={'titre': 'Le Petit Prince'})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {'message': 'Livre non trouvé ou déjà retourné'})

         # Test retounrer un livre non emprunte
        response = self.client.post('/retourner', json={'titre': 'Les Misérables'})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {'message': 'Livre non trouvé ou déjà retourné'})
       
if __name__ == '__main__':
    unittest.main()
