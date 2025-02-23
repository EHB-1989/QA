# -*-coding:utf-8 -*-
'''
@File    :   test_blog_app.py
@Time    :   2025/01/27 16:04:44
@Author  :   FOURMONT Baptiste
@Version :   1.0
@Contact :   baptiste_fourmont@tutanota.com
@Desc    :   None
'''

from database_manager import DBManager
from poster import Poster
import os
import unittest

class TestPosterDatabase(unittest.TestCase):
    def setUp(self):
        db_name = "test.db"
        self.db = DBManager(db_name=db_name)

    def test_add_posts(self):
        post = Poster("title", "content")
        post2 = Poster("title2", "content2")
        self.db.add_post(post)
        self.db.add_post(post2)
        posts = self.db.get_posts()
        self.assertEqual(len(posts), 2)
        posts_tuples = [(p.title, p.content) for p in posts]
        self.assertIn((post.title, post.content), posts_tuples)
    
    def test_get_posts_empty(self):
        posts = self.db.get_posts()
        self.assertEqual(len(posts), 2)

if __name__ == "__main__":
    unittest.main()
    