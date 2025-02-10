import unittest
from gestionnaire_de_taches import GestionnaireDeTaches
from utilisateur import Utilisateur
from tache import Tache

from app import app

class TestIntegrationGestionApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def creer_utilisateur_test(self):
        utilisateur = {
            "email" : "test@gmail.com",
            "nom" : "omar_test"
        }
        reponse = self.client.post("/utilisateurs", json = utilisateur)
        self.assertEqual(reponse.status_code, 201)
        self.assertEqual(reponse.json["reponse"], "Utilisateur créé avec succès")

    def taches_test(self):
        tache = {
            "titre" : "test titre",
            "description" : "test description",
            "utilisateur_email": "test@gmail.com"
        }
        reponse = self.client.post("/utilisateurs", json = tache)
        self.assertEqual(reponse.status_code, 201)
        self.assertEqual(reponse.json["reponse"], "Tâche ajoutée avec succès")

    def taches_user_test(self):
        email = "test@gmail.com"
        reponse = self.client.get(f"/utilisateurs/{email}")
        self.assertEqual(reponse.status_code, 200 )

if __name__ == "__main__":
    unittest.main() 
