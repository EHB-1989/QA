#!/usr/bin/env python3
# -*-coding:utf-8 -*-
'''
@File    :   test_integration_reservation.py
@Time    :   2025/02/10 14:39:07
@Author  :   FOURMONT Baptiste
@Version :   1.0
@Contact :   baptiste_fourmont@tutanota.com
@Desc    :   None
'''
import unittest
from chambre import *
from reservation import *

class TestsReservation(unittest.TestCase):
    def setUp(self):
        self.ch1 = Chambre(1, 10)
        self.ch2 = Chambre(2, 100)

    # Réserver une chambre
    def test_reserver(self):
        resa_ch1 = Reservation(self.ch1, 7, 0)
        resa_ch2 = Reservation(self.ch2, 3, 10)
        self.assertEqual(resa_ch1.calculer_cout(), 70)
        self.assertEqual(resa_ch2.calculer_cout(), 270)

    # Annuler la réservation
    def test_annuler(self):
        resa_ch1 = Reservation(self.ch1, 7, 0)
        resa_ch1.annuler(0)
        self.assertTrue(resa_ch1.est_annulee)
        self.assertEqual(resa_ch1.calculer_cout(), 0)
        self.assertEqual(resa_ch1.annuler(0), 0)
        self.assertNotEqual(resa_ch1.annuler(10), 0)

        resa_ch2 = Reservation(self.ch2, 3, 10)
        self.assertFalse(resa_ch2.est_annulee)

    # Définir le prix de la saison
    def test_definir_prix_saison(self):
        self.ch1.definir_prix_saison(1.5)
        self.assertEqual(self.ch1.prix_saison, 15)
        self.ch2.definir_prix_saison(0.5)
        self.assertEqual(self.ch2.prix_saison, 50)

if __name__ == "__main__":
    unittest.main()
