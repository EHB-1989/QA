import unittest
from app import *

#TODO: REFAIRE LOL PCQ CA MARCHE PAS BROSKI

class TestBlogAppAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def test_get_posts(self):
        response = self.client.get("/posts")
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertIsInstance(response, 4)

    def test_add_post(self):
        before = len(self.client.get("/posts").get_json())

        response = self.client.post("/posts", json={"title": "MJackson123", "content": "Heehee"})
        self.assertEqual(response.status_code, 201)

        self.assertEqual(before + 1, len(self.client.get("/posts").get_json()))

