import unittest
from panier import Panier 
from produit import Produit

class TestIntegrationPanierProduit(unittest.TestCase):

    def setUp(self):
        """Initialisation des produits et du panier pour les tests."""
        self.produit1 = Produit("Chocolat", 5.0, 10, 10)  # 10% de remise
        self.produit2 = Produit("Biscuit", 2.5, 20, 0)    # Pas de remise
        self.produit3 = Produit("Jus de fruit", 3.0, 5, 20)  # 20% de remise
        self.panier = Panier()

    def test_ajout_produit_au_panier(self):
        """Test de l'ajout de produits au panier."""
        self.panier.ajouter_produit(self.produit1, 2)  # Ajout de 2 Chocolats
        self.assertEqual(self.panier.produits[self.produit1], 2)
        self.assertEqual(self.produit1.quantite_en_stock, 8)  # Stock mis à jour

    def test_ajout_plusieurs_produits_au_panier(self):
        """Test de l'ajout de plusieurs produits différents au panier."""
        self.panier.ajouter_produit(self.produit1, 2)  # Ajout de 2 Chocolats
        self.panier.ajouter_produit(self.produit2, 5)  # Ajout de 5 Biscuits
        self.assertEqual(self.panier.produits[self.produit1], 2)
        self.assertEqual(self.panier.produits[self.produit2], 5)
        self.assertEqual(self.produit1.quantite_en_stock, 8)
        self.assertEqual(self.produit2.quantite_en_stock, 15)

    def test_ajout_produit_stock_insuffisant(self):
        """Test de l'ajout d'un produit avec un stock insuffisant."""
        self.panier.ajouter_produit(self.produit3, 10)  # Tentative d'ajouter 10 Jus de fruit
        self.assertNotIn(self.produit3, self.panier.produits)  # Ne doit pas être ajouté
        self.assertEqual(self.produit3.quantite_en_stock, 5)  # Stock inchangé

    def test_calcul_total_avec_remise(self):
        """Test du calcul du total avec application des remises."""
        self.panier.ajouter_produit(self.produit1, 2)  # 2 x Chocolat
        self.panier.ajouter_produit(self.produit2, 4)  # 4 x Biscuit
        self.panier.ajouter_produit(self.produit3, 2)  # 2 x Jus de fruit
        total_attendu = (
            2 * self.produit1.calculer_prix_apres_remise() +
            4 * self.produit2.calculer_prix_apres_remise() +
            2 * self.produit3.calculer_prix_apres_remise()
        )
        self.assertAlmostEqual(self.panier.calculer_total(), total_attendu)

    def test_panier_vide(self):
        """Test du calcul du total pour un panier vide."""
        self.assertEqual(self.panier.calculer_total(), 0)

    def test_ajout_produit_plusieurs_fois(self):
        """Test de l'ajout d'un même produit plusieurs fois."""
        self.panier.ajouter_produit(self.produit1, 2)  # Ajout initial de 2 Chocolats
        self.panier.ajouter_produit(self.produit1, 3)  # Ajout supplémentaire de 3 Chocolats
        self.assertEqual(self.panier.produits[self.produit1], 5)
        self.assertEqual(self.produit1.quantite_en_stock, 5)  # Stock correctement mis à jour

if __name__ == "__main__":
    unittest.main()
