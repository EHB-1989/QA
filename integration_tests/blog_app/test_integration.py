import unittest
from integration_tests.blog_app.database_manager.database_manager import DBManager
from integration_tests.blog_app.poster import Poster





test_db = DBManager('test.db')


class TestIntegration(unittest.TestCase):
    def test_ajout_post(self): 
        post1 = Poster('Post 1', 'Content 1')
        test_db.add_post(post1)
        post2 = Poster('Post 2', 'Content 2')
        test_db.add_post(post2)
        getPosts = test_db.get_posts()
        self.assertEqual(len(getPosts), 2)
        self.assertEqual(getPosts[0].title, 'Post 1')
        self.assertEqual(getPosts[0].content, 'Content 1')





