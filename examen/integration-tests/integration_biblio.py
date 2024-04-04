import os
import tempfile
import unittest
from flask_testing import TestCase
from app import app, init_db
from database_manager import get_db_connection, DATABASE_NAME

class TestIntegrationBibliotheque(TestCase):

    def create_app(self):
        # Configurer Flask pour tester
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['DATABASE'] = tempfile.mkstemp()[1]
        return app

    def setUp(self):
        # Initialiser la base de données pour chaque test
        with app.app_context():
            init_db()

    def tearDown(self):
        # Supprimer la base de données temporaire après chaque test
        os.unlink(app.config['DATABASE'])

    def test_ajouter_lister_livres(self):
        # Test pour ajouter un livre et le retrouver dans la liste des livres
        response = self.client.post('/ajouter', json={'titre': 'Test Livre', 'auteur': 'Test Auteur'})
        self.assertEqual(response.status_code, 201)
        response = self.client.get('/livres')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Livre', response.data.decode())

    def test_emprunter_retourner_livre(self):
        # Test pour emprunter un livre et le retourner
        self.client.post('/ajouter', json={'titre': 'Livre Emprunt', 'auteur': 'Auteur'})
        response = self.client.post('/emprunter', json={'titre': 'Livre Emprunt'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('emprunté avec succès', response.data.decode())

        response = self.client.post('/retourner', json={'titre': 'Livre Emprunt'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('retourné avec succès', response.data.decode())

if __name__ == '__main__':
    unittest.main()
