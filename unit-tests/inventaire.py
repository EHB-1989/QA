import unittest
class Inventaire:
    def __init__(self):
        self.produits = {}
 
    def ajouter_produit(self, nom, quantite):
        if quantite <= 0:
            return False
        if nom in self.produits:
            self.produits[nom] += quantite
        else:
            self.produits[nom] = quantite
        return True

    def supprimer_produit(self, nom, quantite):
        if nom not in self.produits or quantite <= 0 or self.produits[nom] < quantite:
            return False
        self.produits[nom] -= quantite
        if self.produits[nom] == 0:
            del self.produits[nom]
        return True

    def rechercher_produit(self, nom):
        return self.produits.get(nom, 0)

class TestInventaire(unittest.TestCase):
    def setUp(self):
        self.inv = Inventaire()
    
    def test_ajouter_produit(self):
        self.assertTrue(self.inv.ajouter_produit("banane", 2))

    def test_supprimer_produit(self):
        self.assertFalse(self.inv.supprimer_produit("tomate", 1))
        self.assertFalse(self.inv.supprimer_produit("banane", 4))
    
    def test_rechercher_produit(self):
        self.inv.ajouter_produit("banane", 2)
        self.assertEqual(self.inv.rechercher_produit("banane"), 2)
        self.assertEqual(self.inv.rechercher_produit("pomme"), 0)

if __name__ == "__main__":
    unittest.main()