import unittest

class TestEmail(unittest.TestCase):
    def test_email(self):
        self.assertTrue(is_valid_email('arnaud@gmail.com')) # True
        self.assertFalse(is_valid_email('arnaud@gmail')) # False