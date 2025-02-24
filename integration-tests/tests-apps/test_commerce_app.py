import unittest
from src.panier import Panier
from src.produit import Produit

class TestPanierEtProduit(unittest.TestCase):

    def setUp(self):
        self.produit1 = Produit("Laptop", 1000, 5)
        self.produit2 = Produit("Souris", 50, 10, 10)  
        self.panier = Panier()

    def test_ajouter_produit_stock_suffisant(self):
        self.panier.ajouter_produit(self.produit1, 2)
        self.assertEqual(self.panier.produits[self.produit1], 2)
        self.assertEqual(self.produit1.quantite_en_stock, 3)

    def test_ajouter_produit_stock_insuffisant(self):
        self.panier.ajouter_produit(self.produit1, 10)
        self.assertNotIn(self.produit1, self.panier.produits)

    def test_calculer_prix_apres_remise(self):
        self.assertEqual(self.produit2.calculer_prix_apres_remise(), 45.0)

    def test_calculer_total(self):
        self.panier.ajouter_produit(self.produit1, 2)  
        self.panier.ajouter_produit(self.produit2, 2) 
        self.assertEqual(self.panier.calculer_total(), 2090)

    def test_acheter_produit(self):
        result = self.produit1.acheter(3)
        self.assertTrue(result)
        self.assertEqual(self.produit1.quantite_en_stock, 2)

    def test_acheter_produit_stock_insuffisant(self):
        result = self.produit1.acheter(10)
        self.assertFalse(result)
        self.assertEqual(self.produit1.quantite_en_stock, 5)

if __name__ == '__main__':
    unittest.main()
