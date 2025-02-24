import unittest
import json
import os
from blog_app.app import app
from blog_app.database_manager import init_db, ajouter_livre_db, get_db_connection

class TestFlaskApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_db = "test_bibliotheque.db"
        cls.app = app.test_client()  # Client de test Flask
        cls.app.testing = True

        # Remplace la connexion avec une base de test
        os.remove("bibliotheque.db") if os.path.exists("bibliotheque.db") else None
        init_db()

    @classmethod
    def tearDownClass(cls):
        os.remove("bibliotheque.db")  # Supprime la base de test

    def test_ajouter_livre(self):
        livre = {"titre": "1984", "auteur": "George Orwell"}
        response = self.app.post('/ajouter', data=json.dumps(livre), content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"message": "Livre ajouté avec succès"})

    def test_lister_livres(self):
        # Ajouter un livre pour le test
        ajouter_livre_db("Le Petit Prince", "Antoine de Saint-Exupéry")

        response = self.app.get('/livres')
        data = response.json

        self.assertEqual(response.status_code, 200)
        self.assertTrue(any(livre["titre"] == "Le Petit Prince" for livre in data))

    def test_emprunter_livre(self):
        ajouter_livre_db("Les Misérables", "Victor Hugo")

        response = self.app.post('/emprunter', data=json.dumps({"titre": "Les Misérables"}), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Livre emprunté avec succès"})

    def test_emprunter_livre_non_disponible(self):
        response = self.app.post('/emprunter', data=json.dumps({"titre": "Livre Inexistant"}), content_type='application/json')

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"message": "Livre non disponible"})

    def test_retourner_livre(self):
        ajouter_livre_db("Harry Potter", "J.K. Rowling")

        self.app.post('/emprunter', data=json.dumps({"titre": "Harry Potter"}), content_type='application/json')
        response = self.app.post('/retourner', data=json.dumps({"titre": "Harry Potter"}), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Livre retourné avec succès"})

if __name__ == '__main__':
    unittest.main()
