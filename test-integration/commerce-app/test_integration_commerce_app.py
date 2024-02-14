import unittest
from panier import *
from produit import *

class TestCommerce(unittest.TestCase):
    panier = Panier()
    tomate = Produit("tomate",10,1,10)
    patate = Produit("patate",20,0.5,10)

    def test_ajout(self):
        self.panier.add(self.tomate, 4)
        self.assertEqual(self.panier.getTotal(), 4)


if __name__ == '__main__':
    unittest.main()   