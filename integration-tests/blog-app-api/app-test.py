import unittest
from unittest.mock import patch
from app import app
from poster import Poster

class TestBlogAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('app.db_manager')
    def test_create_post(self, mock_db):
        test_post = {
            "title": "Test Title",
            "content": "Test Content"
        }

        response = self.app.post('/posts', json=test_post)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.json,
            {"message": "Post added successfully"}
        )

    @patch('app.db_manager')
    def test_get_posts(self, mock_db):
        mock_posts = [
            Poster("Title 1", "Content 1"),
            Poster("Title 2", "Content 2")
        ]
        mock_db.get_posts.return_value = mock_posts

        response = self.app.get('/posts')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 2)
        self.assertEqual(response.json[0]["title"], "Title 1")
        self.assertEqual(response.json[1]["content"], "Content 2")

if __name__ == '__main__':
    unittest.main()