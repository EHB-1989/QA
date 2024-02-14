from poster import Poster
from database_manager import DBManager

import unittest
import requests

class MyTest(unittest.TestCase):

    def test(self):

       url = "http://127.0.0.1:5000/posts"
       body = {"title":"title1", "content":"test"}

       req = requests.post(url, json=body)
       
       req2 = requests.get(url)
       self.assertEqual(req2, {"title": "title1", "content": "test"})



if __name__ == '__main__':
    unittest.main()
