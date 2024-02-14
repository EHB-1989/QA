import unittest
from produit import *
from panier import *

class TestIntegrationPanierProduit(unittest.TestCase):
    def test_integration_ajouter_produit(self):
        produit_1 = Produit("pomme", 10, 5)
        produit_2 = Produit("banane", 20, 10, 10)
        panier = Panier()

        panier.ajouter_produit(produit_1, 2)
        panier.ajouter_produit(produit_2, 1)

        self.assertEqual(panier.produits[produit_1], 2)
        self.assertEqual(panier.produits[produit_2], 1)

    def test_integration_calculer_total(self):
        produit_1 = Produit("pomme", 10, 5)
        produit_2 = Produit("banane", 20, 10, 10) 
        panier = Panier()

        panier.ajouter_produit(produit_1, 2)
        panier.ajouter_produit(produit_2, 1)

        expected_total = (produit_1.calculer_prix_apres_remise() * 2) + (produit_2.calculer_prix_apres_remise() * 1)
        self.assertEqual(panier.calculer_total(), expected_total)

if __name__ == '__main__':
    unittest.main()
