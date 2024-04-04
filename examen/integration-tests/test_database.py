import unittest
import os
from flask_testing import TestCase
from app import app, init_db, ajouter_livre_db, emprunter_livre_db

class TestFlaskApp(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['DATABASE_NAME'] = "test_bibliotheque.db"  
        return app

    def setUp(self):
        init_db()
        ajouter_livre_db('Les Misérables', 'Victor Hugo')

    def test_ajouter_livre(self):
        response = self.client.post('/ajouter', json={'titre': 'Test Livre', 'auteur': 'Test Auteur'})
        self.assertEqual(response.status_code, 201)

    def test_lister_livres(self):
        response = self.client.get('/livres')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(any('Les Misérables' in livre['titre'] for livre in response.json))

    def test_emprunter_livre_succes(self):
        response = self.client.post('/emprunter', json={'titre': 'Les Misérables'})
        self.assertEqual(response.status_code, 200)

    def test_emprunter_livre_echec(self):
        self.client.post('/emprunter', json={'titre': 'Les Misérables'})  
        response = self.client.post('/emprunter', json={'titre': 'Les Misérables'})
        self.assertEqual(response.status_code, 404)

    def test_retourner_livre_succes(self):
        self.client.post('/emprunter', json={'titre': 'Les Misérables'})
        response = self.client.post('/retourner', json={'titre': 'Les Misérables'})
        self.assertEqual(response.status_code, 200)

    def test_retourner_livre_echec(self):
        response = self.client.post('/retourner', json={'titre': 'Unborrowed Book'})
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
