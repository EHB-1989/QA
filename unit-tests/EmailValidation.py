import re
import unittest

def is_valid_email(email):
    return bool(re.match(r"^[\w\.-]+@[\w\.=]+$", email))

class TestEmailValidation(unittest.TestCase):
    def test_valid_emails(self):
        self.assertTrue(is_valid_email("exampke@example.com"))
        self.assertTrue(is_valid_email("username@gmail.com"))
        self.assertTrue(is_valid_email("test.test@mot="))

    def test_invalid_emails(self):
        self.assertFalse(is_valid_email("example.example.com"))
        self.assertFalse(is_valid_email("example@"))
        self.assertFalse(is_valid_email("mot"))

if __name__ == "__main__":
    unittest.main()