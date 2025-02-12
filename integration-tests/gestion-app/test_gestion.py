import unittest
import requests

BASE_URL = "http://127.0.0.1:5000"

class TestGestionTachesAPI(unittest.TestCase):
    
    def test_ajout_utilisateur_et_tache(self):
        # Données de l'utilisateur
        utilisateur_data = {"nom": "Jean Dupont", "email": "jean.dupont@example.com"}
        response = requests.post(f"{BASE_URL}/utilisateurs", json=utilisateur_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["message"], "Utilisateur créé avec succès")
        
        # Données de la tâche
        tache_data = {
            "titre": "Acheter du lait",
            "description": "Aller au supermarché pour acheter du lait",
            "utilisateur_email": "jean.dupont@example.com"
        }
        response = requests.post(f"{BASE_URL}/taches", json=tache_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["message"], "Tâche ajoutée avec succès")
        
        # Vérification de la récupération des tâches
        response = requests.get(f"{BASE_URL}/taches/jean.dupont@example.com")
        self.assertEqual(response.status_code, 200)
        taches = response.json()
        self.assertIn(tache_data, taches)

if __name__ == "__main__":
    unittest.main()
