import unittest

from poster import Poster
from database_manager import DBManager

class TestBlogApp(unittest.TestCase):
    def setUp(self):
        self.db_manager = db_manager("testDB")
        self.poster1 = Poster("Title1", "Content1")
        self.poster2 = Poster("Title2", "Content2")

    def test_add_post(self):
        self.db_manager.add_post(self.poster1)
        self.db_manager.add_post(self.poster2)
        self.assertEqual(self.db_manager.get_posts(), [self.poster1, self.poster2])

if __name__ == '__main__':
    unittest.main()