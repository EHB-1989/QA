import unittest
import os
from app import app, init_db, get_db_connection

TEST_DB = "test_bibliotheque.db"

class TestBibliothequeIntegration(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Configuration of the test environment."""
        app.config['TESTING'] = True
        app.config['DATABASE'] = TEST_DB
        cls.client = app.test_client()
        init_db()
    
    def setUp(self):
        """Reset the database before each test."""
        with get_db_connection() as conn:
            conn.execute('DELETE FROM livres')
            conn.executemany('INSERT INTO livres (titre, auteur, est_emprunte) VALUES (?, ?, ?)', [
                ('Naruto', 'Masashi Kishimoto', False),
                ('Dragon Ball', 'Akira Toriyama', False)
            ])
    
    def test_add_book(self):
        response = self.client.post('/ajouter', json={
            'titre': 'One Piece', 'auteur': 'Eiichirō Oda'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Livre ajouté avec succès', response.get_json()['message'])
    
    def test_list_books(self):
        response = self.client.get('/livres')
        self.assertEqual(response.status_code, 200)
        livres = response.get_json()
        self.assertGreaterEqual(len(livres), 2)
    
    def test_borrow_book_success(self):
        response = self.client.post('/emprunter', json={'titre': 'Naruto'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Livre emprunté avec succès', response.get_json()['message'])
    
    def test_borrow_book_already_borrowed(self):
        self.client.post('/emprunter', json={'titre': 'Naruto'})
        response = self.client.post('/emprunter', json={'titre': 'Naruto'})
        self.assertEqual(response.status_code, 404)
        self.assertIn('Livre non disponible', response.get_json()['message'])
    
    def test_return_book_success(self):
        self.client.post('/emprunter', json={'titre': 'Dragon Ball'})
        response = self.client.post('/retourner', json={'titre': 'Dragon Ball'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Livre retourné avec succès', response.get_json()['message'])
    
    def test_return_book_not_borrowed(self):
        response = self.client.post('/retourner', json={'titre': 'Naruto'})
        self.assertEqual(response.status_code, 404)
        self.assertIn('Livre non trouvé ou déjà retourné', response.get_json()['message'])
    
    @classmethod
    def tearDownClass(cls):
        """Clean up : delete the test database."""
        if os.path.exists(TEST_DB):
            os.remove(TEST_DB)

if __name__ == '__main__':
    unittest.main()
