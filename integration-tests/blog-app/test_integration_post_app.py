import unittest
from poster import Poster
from database_manager import DBManager

class TestDatabaseIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db_manager = DBManager(':memory:')  # Utiliser une base de données en mémoire pour le test

    def test_add_and_get_post(self):
        post = Poster("Test Title", "Test content")
        self.db_manager.add_post(post)

        posts = self.db_manager.get_posts()
        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0].title, "Test Title")
        self.assertEqual(posts[0].content, "Test content")

if __name__ == '__main__':
    unittest.main()
