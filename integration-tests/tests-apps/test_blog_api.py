import unittest
import json
import os
from blog-app-api.app import app, db_manager
from blog-app-api.poster import Poster

class TestFlaskApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_db = "test_blog.db"
        cls.app = app.test_client() 
        cls.app.testing = True
        db_manager.connection.close()  
        os.remove("blog.db")  
        db_manager.__init__(cls.test_db) 

    @classmethod
    def tearDownClass(cls):
        db_manager.__del__()
        os.remove(cls.test_db)

    def test_create_post(self):
        post_data = {"title": "Test Title", "content": "Test Content"}
        response = self.app.post('/posts', data=json.dumps(post_data), content_type='application/json')
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"message": "Post added successfully"})

    def test_get_posts(self):
        db_manager.add_post(Poster("Post 1", "Content 1"))
        
        response = self.app.get('/posts')
        data = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["title"], "Post 1")
        self.assertEqual(data[0]["content"], "Content 1")

if __name__ == '__main__':
    unittest.main()
