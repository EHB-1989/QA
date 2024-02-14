import unittest

from produit import Produit

from panier import Panier

class testPanier(unittest.TestCase):
    def test(self):
        prod1 = Produit('a', 5, 100)
        prod2 = Produit('b', 10, 100)
        pan = Panier()

        pan.ajouter_produit(prod1, 3)
        self.assertTrue(pan.produits == {prod1: 3})
        pan.ajouter_produit(prod2, 2)
        self.assertTrue(pan.produits == {prod1: 3, prod2: 2})
        total = pan.calculer_total()
        expected = prod1.prix * 3 + prod2.prix * 2
        self.assertEqual(total, expected)


if __name__ == '__main__':
    unittest.main()