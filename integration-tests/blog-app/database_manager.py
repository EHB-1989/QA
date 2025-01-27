import sqlite3
from poster import Poster
import unittest

class DBManager:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.connection.execute('CREATE TABLE IF NOT EXISTS posts (title TEXT, content TEXT)')
        self.connection.commit()

    def add_post(self, post):
        self.connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (post.title, post.content))
        self.connection.commit()

    def get_posts(self):
        cursor = self.connection.execute('SELECT title, content FROM posts')
        return [Poster(title, content) for title, content in cursor]

    def __del__(self):
        self.connection.close()

class TestBlog(unittest.TestCase):
    def test_add_and_get_post(self):
        db_manager = DBManager(':memory:')
        post = Poster("Title", "Content")
        db_manager.add_post(post)
        posts = db_manager.get_posts()
        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0].title, "Title")
        self.assertEqual(posts[0].content, "Content")

if __name__ == '__main__':
    unittest.main()