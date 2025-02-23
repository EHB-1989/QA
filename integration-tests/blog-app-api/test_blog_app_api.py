#!/usr/bin/env python3
# -*-coding:utf-8 -*-
'''
@File    :   test_blog_app_api.py
@Time    :   2025/01/27 16:47:01
@Author  :   FOURMONT Baptiste
@Version :   1.0
@Contact :   baptiste_fourmont@tutanota.com
@Desc    :   None
'''

import unittest
from poster import *
from app import app

class TestBlogAppApi(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_create_post(self):
        post_data = {"title": "Test Title", "content": "Test Content"}
        response = self.client.post("/posts", json=post_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"message": "Post added successfully"})

    def test_get_posts(self):
        response = self.client.get("/posts")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [{'content': 'Test Content', 'title': 'Test Title'}])
        print(response.json)


if __name__ == "__main__":
    unittest.main()
    import os 
    if os.path.exists("blog.db"):
        os.remove("blog.db")
