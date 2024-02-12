import unittest

class TestCompteBancaire(unittest.TestCase):
    def setUp(self):
        self.compte = self.CompteBancaire(100)

    def test_depot(self):
        self.assertFalse(self.compte.depot(self, -2))
        self.assertEqual(self.compte.get_solde(), 100)
        self.assertTrue(self.compte.depot(self, 5))
        self.assertEqual(self.compte.get_solde(), 105)

    def test_retrait(self):
        self.assertFalse(self.compte.retrait(self, 200))
        self.assertEqual(self.compte.get_solde(), 105)
        self.assertTrue(self.compte.retrait(self, 50))
        self.assertEqual(self.compte.get_solde(), 55)