#!/usr/bin/env python3
# -*-coding:utf-8 -*-
'''
@File    :   test_integration_commerce.py
@Time    :   2025/02/23 13:58:05
@Author  :   FOURMONT Baptiste
@Version :   1.0
@Contact :   baptiste_fourmont@tutanota.com
@Desc    :   None
'''

import unittest

from panier import *
from produit import *


class TestIntegrationCommerce(unittest.TestCase):
    def setUp(self):
        self.panier = Panier()

    def test_ajouter_produit(self):
        banane = Produit("banane", 10, 2, 20)
        self.panier.ajouter_produit(banane, 2)
        self.assertIn(
            banane, self.panier.produits, "La banane devrait être dans le panier"
        )

        orange = Produit("orange", 1, 10, 10)
        self.panier.ajouter_produit(orange, 5)
        self.assertIn(
            orange, self.panier.produits, "L'orange devrait être dans le panier"
        )
    
    def test_inside_panier(self):
        banane = Produit("banane", 10, 2, 20)
        panier = Panier()
        panier.ajouter_produit(banane, 2)
        orange = Produit("orange", 1, 10, 10)
        panier.ajouter_produit(orange, 5)
        self.assertEqual(panier.produits[banane], 2)
        self.assertEqual(panier.produits[orange], 5)

    def test_calculer_total(self):
        banane = Produit("banane", 10, 2, 20)
        orange = Produit("orange", 1, 10, 80)

        self.panier.ajouter_produit(banane, 2)
        self.panier.ajouter_produit(orange, 5)

        total_attendu = (
            banane.calculer_prix_apres_remise() * 2
            + orange.calculer_prix_apres_remise() * 5
        )
        self.assertEqual(self.panier.calculer_total(), total_attendu)


    def test_acheter(self):
        produit = Produit("Banane", 0.5, 20)
        self.assertTrue(produit.acheter(10))
        self.assertEqual(produit.quantite_en_stock, 10)
        self.assertFalse(produit.acheter(15))
        self.assertEqual(produit.quantite_en_stock, 10)


if __name__ == "__main__":
    unittest.main()
