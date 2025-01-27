import unittest
from app import app
from database_manager import DBManager
from poster import Poster

##tester avec un serveur test_client les différentes routes
## test de la route get
## test de la route post

class TestIntegrationAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_create_post(self):
        data = {
            "title": "Titre Omar Test",
            "content": "Content Omar Test"
        }
        response = self.client.post('/posts', json=data)

        self.assertEqual(response.status_code, 201)
        self.assertIn("message", response.json)
        self.assertEqual(response.json["message"], "Post added successfully")

    def test_get_posts(self):

        post = Poster("Titre Omar Test", "Content Omar Test")
        db = DBManager("blog.db")
        db.add_post(post)  # Méthode pour ajouter directement un post dans la base

        # Envoie une requête GET à l'API
        response = self.client.get('/posts')

        # Vérifie la réponse
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json[0]["title"], "Titre Omar Test")
        self.assertEqual(response.json[0]["content"], "Content Omar Test")

if __name__ == "__main__":
    unittest.main()
