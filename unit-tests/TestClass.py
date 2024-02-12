import unittest
from EmailValidation import *
from CompteBancaire import *
class test_valid_email(unittest.TestCase):
    def test_valid_email(self):
        valid_email = "toto@gmail.com"
        valid_email2 = "toto.titi@free.com"
        self.assertTrue(is_valid_email(valid_email))
        self.assertTrue(is_valid_email(valid_email2))

    def test_unvalid_email(self):
        unvalid_email = "toto.com"
        unvalid_email2 = "toto@gmail@titi.com"

        self.assertFalse(is_valid_email(unvalid_email))
        self.assertFalse(is_valid_email(unvalid_email2))

class test_compte(unittest.TestCase):
    compte = CompteBancaire(-150)
    def test_retrait_solde_negatif(self):
        self.assertFalse(self.compte.retrait(-350))
        print(self.compte.get_solde())
if __name__ == '__main__':
    unittest.main()
