import unittest
import os
import json
from app import app
import database_manager

class BibliothequeIntegrationTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Utilise une base de données de test
        database_manager.DATABASE_NAME = "test_bibliotheque.db"
        # Configure le client de test Flask
        app.config['TESTING'] = True
        cls.client = app.test_client()

    def setUp(self):
        # S'assurer que la base de test est propre avant chaque test
        try:
            conn = database_manager.get_db_connection()
            conn.execute("DROP TABLE IF EXISTS livres")
            conn.commit()
            conn.close()
        except Exception:
            pass
        database_manager.init_db()

    def test_lister_livres(self):
        # init_db ajoute 3 livres par défaut
        response = self.client.get('/livres')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 3)
        self.assertEqual(data[0]['titre'], 'Les Misérables')

    def test_ajouter_livre(self):
        payload = {'titre': 'Le Seigneur des Anneaux', 'auteur': 'J.R.R. Tolkien'}
        response = self.client.post('/ajouter', 
                                    data=json.dumps(payload), 
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'], 'Livre ajouté avec succès')

        # Vérifier que le livre a bien été ajouté
        response2 = self.client.get('/livres')
        data = json.loads(response2.data)
        self.assertEqual(len(data), 4)
        titres = [livre['titre'] for livre in data]
        self.assertIn('Le Seigneur des Anneaux', titres)

    def test_emprunter_livre_succes(self):
        payload = {'titre': 'Les Misérables'}
        response = self.client.post('/emprunter', 
                                    data=json.dumps(payload), 
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'], 'Livre emprunté avec succès')

        # Vérifier l'état dans la base de données
        conn = database_manager.get_db_connection()
        livre = conn.execute("SELECT * FROM livres WHERE titre='Les Misérables'").fetchone()
        conn.close()
        self.assertTrue(livre['est_emprunte'])

    def test_emprunter_livre_indisponible(self):
        # Emprunter une première fois
        payload = {'titre': 'Les Misérables'}
        self.client.post('/emprunter', data=json.dumps(payload), content_type='application/json')
        
        # Emprunter une deuxième fois
        response = self.client.post('/emprunter', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 404)
        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'], 'Livre non disponible')

    def test_emprunter_livre_inexistant(self):
        payload = {'titre': 'Livre Inexistant'}
        response = self.client.post('/emprunter', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_retourner_livre_succes(self):
        payload = {'titre': '1984'}
        # Emprunter puis retourner
        self.client.post('/emprunter', data=json.dumps(payload), content_type='application/json')
        response = self.client.post('/retourner', data=json.dumps(payload), content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'], 'Livre retourné avec succès')

        # Vérifier l'état dans la base de données
        conn = database_manager.get_db_connection()
        livre = conn.execute("SELECT * FROM livres WHERE titre='1984'").fetchone()
        conn.close()
        self.assertFalse(livre['est_emprunte'])

    def test_retourner_livre_non_emprunte(self):
        payload = {'titre': '1984'}
        response = self.client.post('/retourner', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 404)
        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'], 'Livre non trouvé ou déjà retourné')

if __name__ == '__main__':
    unittest.main()
