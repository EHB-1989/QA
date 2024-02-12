import unittest
from EmailValidation import is_valid_email


class TestIsValidEmail(unittest.TestCase):
       
 def test_valid_emails(mail):

        valid_email = "test@example.com"
       
        mail.assertTrue(is_valid_email(valid_email))


 def test_invalid_emails(mail):
        
        invalid_email = "tata.email.com"

        mail.assertFalse(is_valid_email(invalid_email))


if __name__ == "__main__":
    unittest.main()