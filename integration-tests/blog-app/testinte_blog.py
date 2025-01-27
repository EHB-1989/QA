import unittest
from poster import Poster
import os
from database_manager import DBManager

class TestDBManagerIntegration(unittest.TestCase):
    #TEST
    @classmethod
    def setUpClass(cls):
        """Définit le nom de la base de données temporaire pour les tests."""
        cls.test_db = "test_posts.db"

    def setUp(self):
        """Initialise un nouveau DBManager avant chaque test."""
        self.db = DBManager(self.test_db)

    def tearDown(self):
        """Ferme la connexion et supprime la base de données après chaque test."""
        self.db.__del__
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_add_and_get_posts(self):
        """Vérifie qu'on peut ajouter des posts et les récupérer correctement."""
        post1 = Poster("Post 1", "Ceci est le contenu du post 1.")
        post2 = Poster("Post 2", "Ceci est le contenu du post 2.")

        self.db.add_post(post1)
        self.db.add_post(post2)

        posts = self.db.get_posts()
        self.assertEqual(len(posts), 2)
        self.assertEqual(posts[0].title, "Post 1")
        self.assertEqual(posts[0].content, "Ceci est le contenu du post 1.")
        self.assertEqual(posts[1].title, "Post 2")
        self.assertEqual(posts[1].content, "Ceci est le contenu du post 2.")

    def test_empty_database(self):
        """Vérifie que récupérer des posts dans une base vide renvoie une liste vide."""
        posts = self.db.get_posts()
        self.assertEqual(posts, [])

    def test_add_post_with_same_title(self):
        """Vérifie qu'on peut ajouter plusieurs posts avec le même titre."""
        post1 = Poster("Post Identique", "Contenu 1.")
        post2 = Poster("Post Identique", "Contenu 2.")

        self.db.add_post(post1)
        self.db.add_post(post2)

        posts = self.db.get_posts()
        self.assertEqual(len(posts), 2)
        self.assertEqual(posts[0].title, "Post Identique")
        self.assertEqual(posts[0].content, "Contenu 1.")
        self.assertEqual(posts[1].title, "Post Identique")
        self.assertEqual(posts[1].content, "Contenu 2.")

    def test_persistence(self):
        """Vérifie que les données sont correctement persistées dans la base de données."""
        post = Poster("Post Persistant", "Ceci est un test de persistance.")
        self.db.add_post(post)

        self.db.__del__
        self.db = DBManager(self.test_db)

        posts = self.db.get_posts()
        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0].title, "Post Persistant")
        self.assertEqual(posts[0].content, "Ceci est un test de persistance.")

if __name__ == "__main__":
    unittest.main()