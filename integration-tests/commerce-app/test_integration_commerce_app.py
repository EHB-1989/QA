import unittest
from produit import Produit
from panier import Panier

class TestIntegrationPanierProduit(unittest.TestCase):
    # def test_ajouter_et_calculer_total(self):
    #     # Création des produits
    #     pomme = Produit("Pomme", 1.0)
    #     banane = Produit("Banane", 1.5)
        
    #     # Création du panier et ajout des produits
    #     panier = Panier()
    #     panier.ajouter_produit(pomme)
    #     panier.ajouter_produit(banane)
        
    #     # Vérification du total
    #     self.assertEqual(panier.calculer_total(), 2.5)

    def test_ajouter_produit_avec_remise_et_stock(self):
        # Création des produits avec stock et remise
        pomme = Produit("Pomme", 1.0, 10, 10)  # 10% de remise
        banane = Produit("Banane", 1.5, 5, 0)  # Pas de remise
        
        # Création du panier et ajout des produits
        panier = Panier()
        panier.ajouter_produit(pomme, 2)  # Acheter 2 pommes
        panier.ajouter_produit(banane, 1)  # Acheter 1 banane
        
        # Vérification du total avec remises et stocks pris en compte
        expected_total = pomme.calculer_prix_apres_remise() * 2 + banane.calculer_prix_apres_remise() * 1
        self.assertEqual(panier.calculer_total(), expected_total)
        self.assertEqual(pomme.quantite_en_stock, 8)  # Vérification de la mise à jour du stock
        self.assertTrue(pomme.acheter(1))  # Vérifie que l'achat est possible
        self.assertFalse(pomme.acheter(10))  # Quantité demandée supérieure au stock


if __name__ == '__main__':
    unittest.main()
