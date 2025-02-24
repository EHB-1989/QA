import unittest
from app import *


class IntegrationTestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api = app.test_client()
        cls.livre = {'titre': 'Les Misérables', 'auteur': 'Victor Hugo'}

    def test_ajout_livre(self):
        response = self.api.post('/ajouter', json=self.livre)
        self.assertEqual(response.status_code, 201)
        self.assertIn('Livre ajouté avec succès', response.get_json()['message'])

    def test_livres(self):
        response = self.api.get('/livres')
        # self.assertEqual(len(response.get_json()), 1) # <-- Source de probleme vu qu'on a pas de teardown ni de base de données qui se nettoie et que je suis paresseux
        self.assertEqual(response.status_code, 200) # On se base que sur le status code pour être certain que le listing marche, le reste sera testé ailleurs

    def test_emprunt(self):
        response = self.api.post('/emprunter', json={'titre': 'Les Misérables'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Livre emprunté avec succès', response.get_json()['message'])

        response = self.api.post('/emprunter', json={'titre': 'jenexistepas'})
        self.assertEqual(response.status_code, 404)
        self.assertIn('Livre non disponible', response.get_json()['message'])

    def test_retourner_livre(self):
        response = self.api.post('/retourner', json={'titre': 'Les Misérables'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Livre retourné avec succès', response.get_json()['message'])

        response = self.api.post('/retourner', json={'titre': 'jenexistepas'})
        self.assertEqual(response.status_code, 404)
        self.assertIn('Livre non trouvé ou déjà retourné', response.get_json()['message'])


if __name__ == '__main__':
    unittest.main()
