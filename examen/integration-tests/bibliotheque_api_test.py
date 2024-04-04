import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_ajouter_livre(self):
        response = self.app.post('/ajouter', json={'titre': 'Harry Potter', 'auteur': 'J.K. Rowling'})
        self.assertEqual(response.status_code, 201)

    def test_lister_livres(self):
        response = self.app.get('/livres')
        self.assertEqual(response.status_code, 200)

    def test_emprunter_livre(self):
        self.app.post('/ajouter', json={'titre': 'Harry Potter', 'auteur': 'J.K. Rowling'})
        response = self.app.post('/emprunter', json={'titre': 'Harry Potter'})
        self.assertEqual(response.status_code, 200)

        response = self.app.post('/emprunter', json={'titre': 'Harry Potter'})
        self.assertEqual(response.status_code, 404)

    def test_retourner_livre(self):
        self.app.post('/ajouter', json={'titre': 'Harry Potter', 'auteur': 'J.K. Rowling'})
        self.app.post('/emprunter', json={'titre': 'Harry Potter'})
        response = self.app.post('/retourner', json={'titre': 'Harry Potter'})
        self.assertEqual(response.status_code, 200)

        response = self.app.post('/retourner', json={'titre': 'Harry Potter'})
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
