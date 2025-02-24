import unittest
import json
from app import app
from gestionnaire_de_taches import GestionnaireDeTaches

class TestGestionAppIntegration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        cls.gestionnaire = GestionnaireDeTaches('test_taches.db')
        
        cls.gestionnaire.conn.execute('DROP TABLE IF EXISTS taches')
        cls.gestionnaire.conn.execute('DROP TABLE IF EXISTS utilisateurs')
        cls.gestionnaire.conn.commit()
        cls.gestionnaire.__init__('test_taches.db') 

    def test_creer_utilisateur(self):
        data = {"nom": "laz ml", "email": "laz.ml@example.com"}
        response = self.client.post('/utilisateurs', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"message": "Utilisateur créé avec succès"})

    def test_ajouter_tache(self):
        utilisateur = {"nom": "Marie Curie", "email": "marie.curie@example.com"}
        self.client.post('/utilisateurs', json=utilisateur)

        tache = {
            "titre": "Faire les courses",
            "description": "Acheter du lait et du pain",
            "utilisateur_email": "marie.curie@example.com"
        }
        response = self.client.post('/taches', json=tache)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"message": "Tâche ajoutée avec succès"})

    def test_recuperer_taches(self):
        utilisateur = {"nom": "Albert Einstein", "email": "albert.einstein@example.com"}
        self.client.post('/utilisateurs', json=utilisateur)

        taches = [
            {"titre": "Étudier la relativité", "description": "Lire le livre sur la relativité", "utilisateur_email": "albert.einstein@example.com"},
            {"titre": "Écrire un article", "description": "Rédiger un article pour la revue scientifique", "utilisateur_email": "albert.einstein@example.com"}
        ]
        for tache in taches:
            self.client.post('/taches', json=tache)

        response = self.client.get('/taches/albert.einstein@example.com')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 2)
        self.assertIn({"titre": "Étudier la relativité", "description": "Lire le livre sur la relativité"}, response.json)
        self.assertIn({"titre": "Écrire un article", "description": "Rédiger un article pour la revue scientifique"}, response.json)

    @classmethod
    def tearDownClass(cls):
        cls.gestionnaire.conn.close()
        import os
        os.remove('test_taches.db')

if __name__ == '__main__':
    unittest.main()
