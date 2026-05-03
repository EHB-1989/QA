import unittest
import os
import json
from app import app
from database_manager import init_db, get_db_connection, DATABASE_NAME


class TestIntegrationBibliotheque(unittest.TestCase):

    def setUp(self):
        self.test_db = "test_bibliotheque.db"
        import database_manager
        database_manager.DATABASE_NAME = self.test_db
        init_db()
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_lister_livres_default(self):
        response = self.app.get('/livres')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 3)

    def test_ajouter_livre(self):
        response = self.app.post('/ajouter', json={
            'titre': 'Germinal',
            'auteur': 'Émile Zola'
        })
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Livre ajouté avec succès')

        response = self.app.get('/livres')
        livres = json.loads(response.data)
        titres = [l['titre'] for l in livres]
        self.assertIn('Germinal', titres)

    def test_emprunter_livre_succes(self):
        response = self.app.post('/emprunter', json={
            'titre': '1984'
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Livre emprunté avec succès')

    def test_emprunter_livre_non_disponible(self):
        self.app.post('/emprunter', json={'titre': '1984'})
        response = self.app.post('/emprunter', json={'titre': '1984'})
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Livre non disponible')

    def test_emprunter_livre_inexistant(self):
        response = self.app.post('/emprunter', json={
            'titre': 'Livre Inexistant'
        })
        self.assertEqual(response.status_code, 404)

    def test_retourner_livre_succes(self):
        self.app.post('/emprunter', json={'titre': 'Le Petit Prince'})
        response = self.app.post('/retourner', json={
            'titre': 'Le Petit Prince'
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Livre retourné avec succès')

    def test_retourner_livre_non_emprunte(self):
        response = self.app.post('/retourner', json={
            'titre': '1984'
        })
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Livre non trouvé ou déjà retourné')

    def test_flux_complet(self):
        self.app.post('/ajouter', json={
            'titre': 'Candide',
            'auteur': 'Voltaire'
        })
        response = self.app.post('/emprunter', json={'titre': 'Candide'})
        self.assertEqual(response.status_code, 200)

        response = self.app.post('/emprunter', json={'titre': 'Candide'})
        self.assertEqual(response.status_code, 404)

        response = self.app.post('/retourner', json={'titre': 'Candide'})
        self.assertEqual(response.status_code, 200)

        response = self.app.post('/emprunter', json={'titre': 'Candide'})
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
