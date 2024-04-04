import unittest
import requests

class TestDatabaseIntegration(unittest.TestCase):
    API = "http://127.0.0.1:5000/"
    
    def test_ajouter_livre(self):
        
        livre = {"titre" : "One piece", "auteur": "Eichiro oda"}
        
        reponse = requests.post(self.API + "/ajouter", json=livre)
        self.assertEqual(reponse.status_code,201)
        
    def test_emprunter_livre(self):
        reponse = requests.post(self.API + "/emprunter", json={"titre":"One piece"})
        self.assertEqual(reponse.status_code,200)
    
    def test_retourner_livre(self):        
        requests.post(self.API + "/emprunter", json={"titre":"One piece"})
        
        reponse = requests.post(self.API + "/retourner", json={"titre":"One piece"})
        self.assertEqual(reponse.status_code,200)
    
    def test_livres(self) :
        reponse = requests.get(self.API + "/livres")
        self.assertEqual(reponse.status_code,200)
        livres = reponse.json()
    
if __name__ == '__main__':
    unittest.main()
