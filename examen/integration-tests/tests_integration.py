import unittest
import requests

class TestLivre(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000"

    def test_ajout_livre_and_list(self):
        livre = {"titre": "Le temps des tempêtes", "auteur": "Sarkozy"}
        response = requests.post(self.API_URL + "/ajouter", json=livre)
        self.assertEqual(response.status_code, 201)

        response = requests.get(self.API_URL + "/livres")
        self.assertIn(livre, response)

    def test_emprunter_livre(self):
        titre = "Le temps des tempêtes"
        response = requests.post(self.API_URL + "/emprunter", json={"titre": titre})
        self.assertEqual(response.status_code, 200)

        titre2 = "Le temps des combats"
        response = requests.post(self.API_URL + "/retourner", json={"titre": titre2})
        self.assertEqual(response.status_code, 404)

    def test_retourner_livre(self):
        titre = "Le temps des tempêtes"
        response = requests.post(self.API_URL + "/retourner", json={"titre": titre})
        self.assertEqual(response.status_code, 200)

        titre2 = "Le temps des combats"
        response = requests.post(self.API_URL + "/retourner", json={"titre": titre2})
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()