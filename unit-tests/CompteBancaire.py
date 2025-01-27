import unittest

class CompteBancaire:
    def __init__(self, solde_initial=0):
        self.solde = solde_initial

    def depot(self, montant):
        if montant > 0:
            self.solde += montant
            return True
        return False

    def retrait(self, montant):
        if montant > 0 and self.solde - montant >= 0:
            self.solde -= montant
            return True
        return False

    def get_solde(self):
        return self.solde

class TestCompteBancaire(unittest.TestCase):
    def test_get_solde(self):
        c = CompteBancaire(100)
        self.assertEqual(c.get_solde(), 100)

    def test_depot(self):
        c = CompteBancaire()
        self.assertTrue(c.depot(100))
        self.assertEqual(c.get_solde(), 100)
        self.assertFalse(c.depot(-100))
        self.assertEqual(c.get_solde(), 100)

    def test_retrait(self):
        c = CompteBancaire(100)
        self.assertTrue(c.retrait(50))
        self.assertEqual(c.get_solde(), 50)
        self.assertFalse(c.retrait(-50))
        self.assertEqual(c.get_solde(), 50)
        self.assertFalse(c.retrait(100))
        self.assertEqual(c.get_solde(), 50)

if __name__ == "__main__":
    unittest.main()