import unittest
from integration_tests.blog_app_api.poster import Poster
from integration_tests.blog_app_api.app import app, db_manager
import os
import json


class TestIntegrationApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Exécuté une seule fois avant tous les tests."""
        # Ici, on commence par utiliseer une base de données temporaire pour les tests
        cls.test_db_name = 'test_blog.db'
        cls.test_db_manager = db_manager.__class__(cls.test_db_name) 
        app.config['TESTING'] = True  
        cls.client = app.test_client()  

    @classmethod
    def tearDownClass(cls):
        """Exécuté une seule fois après tous les tests."""
        del cls.test_db_manager
        if os.path.exists(cls.test_db_name):
            os.remove(cls.test_db_name)  # Ici, on supprime la base de données temporaire

    def test_ajout_post_via_api(self):
        """Test de l'ajout d'un post via l'API POST /posts."""
        post_data = {"title": "Post 1", "content": "Content 1"}
        response = self.client.post('/posts', data=json.dumps(post_data), content_type='application/json')
        self.assertEqual(response.status_code, 201, "L'API devrait retourner un code 201.")
        self.assertIn("Post added successfully", response.get_data(as_text=True), "Le message de succès est incorrect.")

        # Puison vérifie si le post a bien été ajouté à la base de données
        posts = self.test_db_manager.get_posts()
        self.assertEqual(len(posts), 1, "La base de données devrait contenir un post.")
        self.assertEqual(posts[0].title, "Post 1", "Le titre du post ajouté est incorrect.")
        self.assertEqual(posts[0].content, "Content 1", "Le contenu du post ajouté est incorrect.")

    def test_recuperation_posts_via_api(self):
        """Test de la récupération de tous les posts via l'API GET /posts."""
        #Ici on ajoute de plusieurs posts dans la base de données pour les tests
        post1 = Poster('Post A', 'Content A')
        post2 = Poster('Post B', 'Content B')
        self.test_db_manager.add_post(post1)
        self.test_db_manager.add_post(post2)

        response = self.client.get('/posts')
        self.assertEqual(response.status_code, 200, "L'API devrait retourner un code 200.")

        # On finit par vérifier le contenu des posts retournés par l'API
        response_data = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(response_data), 2, "L'API devrait retourner deux posts.")
        self.assertEqual(response_data[0]['title'], 'Post A', "Le titre du premier post est incorrect.")
        self.assertEqual(response_data[1]['content'], 'Content B', "Le contenu du second post est incorrect.")


if __name__ == "__main__":
    unittest.main()
