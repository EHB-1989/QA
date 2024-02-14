import unittest
from CompteBancaire import *

class TestCompteBancaire(unittest.TestCase):
    c = CompteBancaire(22000)
    def test_valid(self):
        self.assertFalse(self.c.retrait(self.c.get_solde()+1))


if __name__ == '__main__':
    unittest.main()   