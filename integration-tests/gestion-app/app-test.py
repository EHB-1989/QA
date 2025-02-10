import unittest
from app import *

class GestionAppTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = app.test_client()

    def test_creer_utilisateur(self):
        response = self.app.post('/args/utilisateurs', json={
            'nom': 'Alice',
            'email': 'alice@gmail.com'
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data.get('message'), "Utilisateur créé avec succès")

    def test_ajout_taches(self):
        response = self.app.post('/args/taches', json={
            'titre': 'Faire les courses',
            'description': 'Acheter du lait, du pain et des oeufs',
            'utilisateur_email': 'alice@gmail.com'
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data.get('message'), "Tâche ajoutée avec succès")

    def test_recuperer_taches(self):
        response = self.app.get("/args/taches/alice@gmail.com")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            'titre': 'Faire les courses',
            'description': 'Acheter du lait, du pain et des oeufs',
            'utilisateur_email': 'alice@gmail.com'
        })


if __name__ == '__main__':
    unittest.main()