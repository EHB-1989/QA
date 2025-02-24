import unittest
from app import app, init_db, get_db_connection

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        # Création du client de test Flask
        self.app = app.test_client()
        # Réinitialiser la base de données avant chaque test
        with get_db_connection() as conn:
            conn.execute('DELETE FROM livres')

    def test_ajouter_livre(self):
        response = self.app.post('/ajouter', json={'titre': 'Le Seigneur des Anneaux', 'auteur': 'J.R.R. Tolkien'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json(), {'message': 'Livre ajouté avec succès'})

    def test_lister_livres(self):
        # Vérifier qu'aucun livre n'est présent au départ
        response = self.app.get('/livres')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 0)
        
        # Ajouter un livre et vérifier qu'il est bien listé
        self.app.post('/ajouter', json={'titre': 'Le Seigneur des Anneaux', 'auteur': 'J.R.R. Tolkien'})
        response = self.app.get('/livres')
        data = response.get_json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['titre'], 'Le Seigneur des Anneaux')

    def test_emprunter_livre(self):
        # Tenter d'emprunter un livre inexistant
        response = self.app.post('/emprunter', json={'titre': 'Le Seigneur des Anneaux'})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json(), {'message': 'Livre non disponible'})
        
        # Ajouter le livre et emprunter
        self.app.post('/ajouter', json={'titre': 'Le Seigneur des Anneaux', 'auteur': 'J.R.R. Tolkien'})
        response = self.app.post('/emprunter', json={'titre': 'Le Seigneur des Anneaux'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Livre emprunté avec succès'})
        
        # Tenter d'emprunter à nouveau (livre déjà emprunté)
        response = self.app.post('/emprunter', json={'titre': 'Le Seigneur des Anneaux'})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json(), {'message': 'Livre non disponible'})

    def test_retourner_livre(self):
        # Tenter de retourner un livre inexistant
        response = self.app.post('/retourner', json={'titre': 'Livre Inexistant'})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json(), {'message': 'Livre non trouvé ou déjà retourné'})
        
        # Ajouter un livre sans l'emprunter, donc impossible de le retourner
        self.app.post('/ajouter', json={'titre': 'Le Seigneur des Anneaux', 'auteur': 'J.R.R. Tolkien'})
        response = self.app.post('/retourner', json={'titre': 'Le Seigneur des Anneaux'})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json(), {'message': 'Livre non trouvé ou déjà retourné'})
        
        # Emprunter puis retourner le livre
        self.app.post('/emprunter', json={'titre': 'Le Seigneur des Anneaux'})
        response = self.app.post('/retourner', json={'titre': 'Le Seigneur des Anneaux'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Livre retourné avec succès'})
        
        # Tenter de retourner à nouveau le même livre
        response = self.app.post('/retourner', json={'titre': 'Le Seigneur des Anneaux'})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json(), {'message': 'Livre non trouvé ou déjà retourné'})

if __name__ == '__main__':
    init_db()  # Initialiser la base de données
    unittest.main()
