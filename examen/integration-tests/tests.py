import unittest
import json
from app import app, init_db
from database_manager import get_db_connection

class TestIntegration(unittest.TestCase):
    # apres avoir essuyé plusieurs echecs j'ai trouvé ces 2 fonctions sur le site : https://docs.python.org/3/library/unittest.html
    def setUp(self):
        self.app = app.test_client()
        init_db()

    def tearDown(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM livres;")
        connection.commit()
        cursor.close()

    def test_ajouter_livre(self):
        response = self.app.post('/ajouter', data=json.dumps({'titre': 'Brave New World', 'auteur': 'Aldous Huxley'}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], 'Livre ajouté avec succès')

    def test_lister_livres(self):
        response = self.app.get('/livres')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Les Misérables', [livre['titre'] for livre in response.json])
        self.assertIn('Le Petit Prince', [livre['titre'] for livre in response.json])
        self.assertIn('1984', [livre['titre'] for livre in response.json])

    def test_emprunter_livre(self):
        response = self.app.post('/emprunter', data=json.dumps({'titre': '1984'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Livre emprunté avec succès')

    def test_emprunter_livre_non_disponible(self):
        self.app.post('/emprunter', data=json.dumps({'titre': '1984'}), content_type='application/json')
        response = self.app.post('/emprunter', data=json.dumps({'titre': '1984'}), content_type='application/json')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], 'Livre non disponible')

    def test_retourner_livre(self):
        self.app.post('/emprunter', data=json.dumps({'titre': 'Le Petit Prince'}), content_type='application/json')
        response = self.app.post('/retourner', data=json.dumps({'titre': 'Le Petit Prince'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Livre retourné avec succès')

    def test_retourner_livre_non_trouve(self):
        response = self.app.post('/retourner', data=json.dumps({'titre': 'Naruto'}), content_type='application/json')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], 'Livre non trouvé ou déjà retourné')

if __name__ == '__main__':
    unittest.main()
