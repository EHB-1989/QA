import unittest
from CompteBancaire import CompteBancaire

class TestCompteBancaire(unittest.TestCase):

    def setUp(self):
        """Initialisation d'un compte pour chaque test."""
        self.compte = CompteBancaire(solde_initial=100)

    def test_initial_balance(self):
        """Test du solde initial."""
        compte = CompteBancaire(solde_initial=200)
        self.assertEqual(compte.get_solde(), 200)

    def test_initial_balance_default(self):
        """Test du solde initial par défaut."""
        compte = CompteBancaire()
        self.assertEqual(compte.get_solde(), 0)

    def test_deposit_positive_amount(self):
        """Test du dépôt avec un montant positif."""
        result = self.compte.depot(50)
        self.assertTrue(result)
        self.assertEqual(self.compte.get_solde(), 150)

    def test_deposit_zero_amount(self):
        """Test du dépôt avec un montant nul."""
        result = self.compte.depot(0)
        self.assertFalse(result)
        self.assertEqual(self.compte.get_solde(), 100)

    def test_deposit_negative_amount(self):
        """Test du dépôt avec un montant négatif."""
        result = self.compte.depot(-50)
        self.assertFalse(result)
        self.assertEqual(self.compte.get_solde(), 100)

    def test_withdraw_positive_amount(self):
        """Test du retrait avec un montant positif valide."""
        result = self.compte.retrait(50)
        self.assertTrue(result)
        self.assertEqual(self.compte.get_solde(), 50)

    def test_withdraw_exact_balance(self):
        """Test du retrait avec un montant égal au solde."""
        result = self.compte.retrait(100)
        self.assertTrue(result)
        self.assertEqual(self.compte.get_solde(), 0)

    def test_withdraw_exceeding_balance(self):
        """Test du retrait avec un montant supérieur au solde."""
        result = self.compte.retrait(150)
        self.assertFalse(result)
        self.assertEqual(self.compte.get_solde(), 100)

    def test_withdraw_zero_amount(self):
        """Test du retrait avec un montant nul."""
        result = self.compte.retrait(0)
        self.assertFalse(result)
        self.assertEqual(self.compte.get_solde(), 100)

    def test_withdraw_negative_amount(self):
        """Test du retrait avec un montant négatif."""
        result = self.compte.retrait(-50)
        self.assertFalse(result)
        self.assertEqual(self.compte.get_solde(), 100)

    def test_get_solde(self):
        """Test de la récupération du solde."""
        self.assertEqual(self.compte.get_solde(), 100)

if __name__ == "__main__":
    unittest.main()
