import unittest
import requests

class TestDB(unittest.TestCase):

    def trouver_livre(self, resp, titre):
        for i in resp:
           if i["titre"] == titre:
               return True
        return False

    def test_ajout_livre(self):
        titre = "Eragon"
        base_url = "http://127.0.0.1:5000/"
        body = {"titre":titre, "auteur":"Auteur"}

        req = requests.post(base_url + "ajouter", json=body)
       
        req2 = requests.get(base_url + "livres")
        resp = req2.json()

        self.assertEqual(req.status_code, 201)

        #Si le livre n'est pas trouvé => test échoué
        self.assertTrue(self.trouver_livre(resp, titre))

    def test_recuperer_livre(self):
        base_url = "http://127.0.0.1:5000/"
        livres = ["Les Misérables", "Le Petit Prince", "1984"]

        req = requests.get(base_url + "livres")
        response = req.json()

        self.assertEqual(req.status_code, 200)

        for l in livres:
            self.assertTrue( self.trouver_livre(response, l))
    
    def test_emprunter_livre(self):
        titre = "Le Petit Prince"
        base_url = "http://127.0.0.1:5000/"

        body = {"titre":titre}

        req = requests.post(base_url + "emprunter", json=body)
        
        self.assertEqual(req.status_code, 200)

        req2 = requests.get(base_url + "livres")
        response = req2.json()

        for i in response:
            if i["titre"] == titre:
                self.assertEqual(i["est_emprunte"], 1)
                return
        self.assertTrue(False) # Livre non trouvé

    def test_rendre_livre(self):
        titre = "Le Petit Prince"
        base_url = "http://127.0.0.1:5000/"

        body = {"titre":titre}

        req = requests.post(base_url + "retourner", json=body)

        self.assertEqual(req.status_code, 200)

        req2 = requests.get(base_url + "livres")
        response = req2.json()

        for i in response:
            if i["titre"] == titre:
                self.assertEqual(i["est_emprunte"], 0)
                return
        self.assertTrue(False) # Livre non trouvé

    def test_rendre_livre_non_emprunte(self):
        titre = "1984"
        base_url = "http://127.0.0.1:5000/"

        body = {"titre":titre}

        req = requests.post(base_url + "retourner", json=body)

        self.assertEqual(req.status_code, 404)

        req2 = requests.get(base_url + "livres")
        response = req2.json()

        for i in response:
            if i["titre"] == titre:
                self.assertEqual(i["est_emprunte"], 0)
                return
        self.assertTrue(False) # Livre non trouvé

    def test_emprunter_livre_deja_emprunte(self):
        titre = "1984"
        base_url = "http://127.0.0.1:5000/"

        body = {"titre":titre}

        req = requests.post(base_url + "emprunter", json=body)

        self.assertEqual(req.status_code, 200)

        req2 = requests.post(base_url + "emprunter", json=body)

        self.assertEqual(req.status_code, 404)

        req3 = requests.get(base_url + "livres")
        response = req3.json()

        for i in response:
            if i["titre"] == titre:
                self.assertEqual(i["est_emprunte"], 1)
                return
        self.assertTrue(False) # Livre non trouvé

        







if __name__ == '__main__':
    unittest.main()
