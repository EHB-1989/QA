import unittest

class TestCommerceApp:
    def setUp(self):
        self.produit1 = self.Produit("Pomme", 1.50, 10)
        self.produit2 = self.Produit("Banane", 1.20, 5, 10)
        self.panier = self.Panier()

    def test_ajouter_produit(self):
        self.panier.ajouter_produit(self.produit1, 5)
        self.assertEqual(self.panier.produits[self.produit1], 5)
        self.panier.ajouter_produit(self.produit2, 3)
        self.assertEqual(self.panier.produits[self.produit2], 3)