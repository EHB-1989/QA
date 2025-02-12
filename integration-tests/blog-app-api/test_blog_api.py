import unittest
import requests

BASE_URL = "http://127.0.0.1:5000"

class TestBlogAPI(unittest.TestCase):
    
    def test_create_and_get_post(self):
        # Données du post
        post_data = {"title": "Test Post", "content": "This is a test post."}
        
        # Envoyer une requête POST pour créer un post
        response = requests.post(f"{BASE_URL}/posts", json=post_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["message"], "Post added successfully")
        
        # Envoyer une requête GET pour récupérer les posts
        response = requests.get(f"{BASE_URL}/posts")
        self.assertEqual(response.status_code, 200)
        
        # Vérifier que le post est bien dans la liste retournée
        posts = response.json()
        self.assertIn(post_data, posts)

if __name__ == "__main__":
    unittest.main()
