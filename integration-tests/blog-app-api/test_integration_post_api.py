import unittest
import requests

class TestAPIIntegration(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000/posts"  # URL de base de l'API

    def test_post_creation_and_retrieval(self):
        # Créer un nouveau post
        post_data = {"title": "Integration Test", "content": "This is a test post."}
        response = requests.post(self.API_URL, json=post_data)
        self.assertEqual(response.status_code, 201)

        # Récupérer tous les posts
        response = requests.get(self.API_URL)
        self.assertEqual(response.status_code, 200)
        posts = response.json()
        self.assertIn(post_data, posts)

if __name__ == '__main__':
    unittest.main()
