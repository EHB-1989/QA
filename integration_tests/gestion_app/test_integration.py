import unittest
import json
import os
from integration_tests.gestion_app.gestionnaire_de_taches import GestionnaireDeTaches
from integration_tests.gestion_app.utilisateur import Utilisateur
from integration_tests.gestion_app.tache import Tache
from integration_tests.gestion_app.app import app

class TestIntegrationApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Exécuté une seule fois avant tous les tests."""
        cls.test_db_name = 'test_taches.db'
        cls.gestionnaire = GestionnaireDeTaches(cls.test_db_name) # Création d'une instance de GestionnaireDeTaches
        app.config['TESTING'] = True # Activation du mode test de Flask
        cls.client = app.test_client()

    @classmethod 
    def tearDownClass(cls):
        """Exécuté une seule fois après tous les tests."""
        del cls.gestionnaire
        if os.path.exists(cls.test_db_name):
            os.remove(cls.test_db_name)  # Suppression de la base de données test

    def test_ajout_utilisateur_via_api(self):
        """Test de la création d'un utilisateur via l'API POST /utilisateurs."""
        utilisateur_data = {"nom": "Alice", "email": "alice@example.com"}
        response = self.client.post('/utilisateurs', data=json.dumps(utilisateur_data), content_type='application/json')
        self.assertEqual(response.status_code, 201, "L'API devrait retourner un code 201.")
        self.assertIn("Utilisateur créé avec succès", response.get_data(as_text=True), "Le message de succès est incorrect.")

    def test_ajout_tache_via_api(self):
        """Test de l'ajout d'une tâche via l'API POST /taches."""
        # On s'assure d'abord que l'utilisateur existe
        utilisateur_data = {"nom": "cr7", "email": "cr7@ballondor.com"}
        self.client.post('/utilisateurs', data=json.dumps(utilisateur_data), content_type='application/json')

        # Ajout de la tâche
        tache_data = {"titre": "Coupe du monde", "description": "Gagner la prochaine Wolrd Cup", "utilisateur_email": "cr7@ballondor.com"}
        response = self.client.post('/taches', data=json.dumps(tache_data), content_type='application/json')
        self.assertEqual(response.status_code, 201, "L'API devrait retourner un code 201.")
        self.assertIn("Tâche ajoutée avec succès", response.get_data(as_text=True), "Le message de succès est incorrect.")

    def test_recuperation_taches_via_api(self):
        """Test de la récupération des tâches via l'API GET /taches/<utilisateur_email>."""
        utilisateur_email = "cr7@ballondor.com"

        # On réalise l'ajout de plusieurs tâches pour l'utilisateur
        self.client.post('/taches', data=json.dumps({"titre": "Faire du sport", "description": "Courir 3000 min", "utilisateur_email": utilisateur_email}), content_type='application/json')
        self.client.post('/taches', data=json.dumps({"titre": "Jeux", "description": "Jouer à Marvel Rivals", "utilisateur_email": utilisateur_email}), content_type='application/json')

        # Récupération des tâches
        response = self.client.get(f'/taches/{utilisateur_email}')
        self.assertEqual(response.status_code, 200, "L'API devrait retourner un code 200.")

        # Enfin, je vérifie du contenu des tâches retournées
        response_data = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(response_data), 2, "L'API devrait retourner deux tâches.")
        self.assertEqual(response_data[0]['titre'], "Faire du sport", "Le titre de la première tâche est incorrect.")
        self.assertEqual(response_data[1]['description'], "Jouer à Marvel Rivals", "La description de la deuxième tâche est incorrecte.")

if __name__ == "__main__":
    unittest.main()
