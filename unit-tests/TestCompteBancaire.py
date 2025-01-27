import unittest
from CompteBancaire import CompteBancaire

class TestCompteBancaire(unittest.TestCase):
    
    def test_initialisation_solde_par_defaut(self):
        compte = CompteBancaire()
        self.assertEqual(compte.get_solde(), 0)

    def test_initialisation_avec_solde_perso(self):
        compte = CompteBancaire(100)
        self.assertEqual(compte.get_solde(), 100)
    #Dépôt ok
    def test_depot_valide(self):
        compte = CompteBancaire(50)
        resultat = compte.depot(50)
        self.assertTrue(resultat)
        self.assertEqual(compte.get_solde(), 100)
    #Dépôt ko
    def test_depot_invalide(self):
        compte = CompteBancaire(50)
        resultat = compte.depot(-10)
        self.assertFalse(resultat)
        self.assertEqual(compte.get_solde(), 50)
    #Retrait ok
    def test_retrait_valide(self):
        compte = CompteBancaire(100)
        resultat = compte.retrait(50)
        self.assertTrue(resultat)
        self.assertEqual(compte.get_solde(), 50)
    #Retrait ko
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