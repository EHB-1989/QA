import unittest
import requests

BASE_URL = "http://127.0.0.1:5000"

class TestAPI(unittest.TestCase):

    def test_1_ajouter_livre(self):
        response = requests.post(f"{BASE_URL}/ajouter", json={
            "titre": "Livre Test",
            "auteur": "Marwan.A"
        })
        self.assertEqual(response.status_code, 201)

    def test_2_lister_livres(self):
        response = requests.get(f"{BASE_URL}/livres")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Livre Test", response.text)

    def test_3_emprunter_livre(self):
        response = requests.post(f"{BASE_URL}/emprunter", json={
            "titre": "Livre Test"
        })
        self.assertEqual(response.status_code, 200)

    def test_4_retourner_livre(self):
        response = requests.post(f"{BASE_URL}/retourner", json={
            "titre": "Livre Test"
        })
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
