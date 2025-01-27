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
    
    def test_initialisation_solde_par_defaut(self):
        compte = CompteBancaire()
        self.assertEqual(compte.get_solde(), 0)

    def test_initialisation_avec_solde_personnalise(self):
        compte = CompteBancaire(100)
        self.assertEqual(compte.get_solde(), 100)

    def test_depot_valide(self):
        compte = CompteBancaire(50)
        resultat = compte.depot(50)
        self.assertTrue(resultat)
        self.assertEqual(compte.get_solde(), 100)

    def test_depot_invalide(self):
        compte = CompteBancaire(50)
        resultat = compte.depot(-10)
        self.assertFalse(resultat)
        self.assertEqual(compte.get_solde(), 50)

    def test_retrait_valide(self):
        compte = CompteBancaire(100)
        resultat = compte.retrait(50)
        self.assertTrue(resultat)
        self.assertEqual(compte.get_solde(), 50)

    def test_retrait_invalide_montant_negatif(self):
        compte = CompteBancaire(100)
        resultat = compte.retrait(-10)
        self.assertFalse(resultat)
        self.assertEqual(compte.get_solde(), 100)

    def test_retrait_invalide_fonds_insuffisants(self):
        compte = CompteBancaire(50)
        resultat = compte.retrait(100)
        self.assertFalse(resultat)
        self.assertEqual(compte.get_solde(), 50)

if __name__ == "__main__":
    unittest.main()