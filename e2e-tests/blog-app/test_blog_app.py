import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Blog', response.data)  

    def test_create_get(self):
        response = self.app.get('/create')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Créer un Article', response.data) 

    def test_create_post(self):
        response = self.app.post('/create', data={'title': 'Test Post', 'content': 'This is a test post.'})
        self.assertEqual(response.status_code, 302) 
        self.assertTrue(response.location.endswith('/'))  

        response = self.app.get('/')
        self.assertIn(b'Test Post', response.data)
        self.assertIn(b'This is a test post.', response.data)

    def test_no_posts(self):
        response = self.app.get('/')
        self.assertIn(b'Blog', response.data)
        self.assertNotIn(b'Test Post', response.data) 

if __name__ == '__main__':
    unittest.main()
