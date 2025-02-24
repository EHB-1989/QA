import unittest
import json
from app import app, init_db

def setUpModule():
    init_db()

class TestIntegrationBibliotheque(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
    
    def test_ajouter_livre_succes(self):
        response = self.client.post('/ajouter', json={"titre": "Test Livre", "auteur": "Auteur Test"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["message"], "Livre ajouté avec succès")
    
    def test_lister_livres(self):
        response = self.client.get('/livres')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
    
    def test_emprunter_livre_succes(self):
        response = self.client.post('/emprunter', json={"titre": "1984"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], "Livre emprunté avec succès")
    
    def test_emprunter_livre_echec(self):
        response = self.client.post('/emprunter', json={"titre": "Un Livre Inexistant"})
        self.assertEqual(response.status_code, 404)
    
    def test_retourner_livre_succes(self):
        response = self.client.post('/retourner', json={"titre": "1984"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], "Livre retourné avec succès")
    
    def test_retourner_livre_echec_deja_retourne(self):
        response = self.client.post('/retourner', json={"titre": "1985"})
        self.assertEqual(response.status_code, 404)
    
    def test_retourner_livre_echec_inexistant(self):
        response = self.client.post('/retourner', json={"titre": "Un Livre Inexistant"})
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
