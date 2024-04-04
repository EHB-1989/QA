import unittest
import requests

class TestAPIIntegration(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000/"  # URL de base de l'API

    def test_ajouter_et_recuperer_livre(self):
        # Créer un nouveau livre
        livre_data = {"titre": "Fairy Tail", "auteur": "Hiro Mashima"}
        response = requests.post(self.API_URL + '/ajouter', json=livre_data)
        self.assertEqual(response.status_code, 201)

        # Récupérer tous les livres
        response = requests.get(self.API_URL + '/livres')
        self.assertEqual(response.status_code, 200)
        livres = response.json()
        self.assertIn({"titre": "Fairy Tail", "auteur": "Hiro Mashima", "est_emprunte": 0, "id": len(livres)}, livres)
        
    def test_emprunter(self):
        livre_data = {"titre": "Fairy Tail"}
        response = requests.post(self.API_URL + '/emprunter', json=livre_data)
        self.assertEqual(response.status_code, 200)
        
        livre_data = {"titre": "My Hero Academia"}
        response = requests.post(self.API_URL + '/emprunter', json=livre_data)
        self.assertEqual(response.status_code, 404)
    
    def test_retourner(self):
        livre_data = {"titre": "Fairy Tail"}
        response = requests.post(self.API_URL + '/retourner', json=livre_data)
        self.assertEqual(response.status_code, 200)
        
        livre_data = {"titre": "My Hero Academia"}
        response = requests.post(self.API_URL + '/retourner', json=livre_data)
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
