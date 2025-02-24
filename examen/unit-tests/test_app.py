#!/usr/bin/env python3
# -*-coding:utf-8 -*-
'''
@File    :   test_app.py
@Time    :   2025/02/24
@Author  :   FOURMONT Baptiste
@Version :   1.0
@Contact :   baptiste_fourmont@tutanota.com
@Desc    :   None
'''

import unittest
from app import Livre, Bibliotheque

class TestLivre(unittest.TestCase):
    def test_emprunter(self):
        livre = Livre("titre", "auteur")
        self.assertTrue(livre.emprunter())
        self.assertFalse(livre.emprunter())

    def test_retourner(self):
        livre = Livre("titre", "auteur")
        self.assertFalse(livre.retourner())
        livre.emprunter()
        self.assertTrue(livre.retourner())

class TestBibliotheque(unittest.TestCase):
    def test_ajouter_livre(self):
        bibliotheque = Bibliotheque()
        livre = Livre("titre", "auteur")
        bibliotheque.ajouter_livre(livre)
        self.assertIn(livre, bibliotheque.livres)
        livre2 = Livre("titre2", "auteur2")
        bibliotheque.ajouter_livre(livre2)
        self.assertEqual(len(bibliotheque.livres), 2)
        # Remove the livre2 because we don't have method remove in Bibliotheque
        bibliotheque.livres.remove(livre2)
        self.assertEqual(len(bibliotheque.livres), 1)
        

    def test_emprunter_livre(self):
        bibliotheque = Bibliotheque()
        livre = Livre("titre", "auteur")
        bibliotheque.ajouter_livre(livre)
        self.assertTrue(bibliotheque.emprunter_livre("titre"))
        self.assertFalse(bibliotheque.emprunter_livre("titre"))

    def test_rendre_livre(self):
        bibliotheque = Bibliotheque()
        livre = Livre("titre", "auteur")
        bibliotheque.ajouter_livre(livre)
        bibliotheque.emprunter_livre("titre")
        self.assertTrue(bibliotheque.retourner_livre("titre"))
        self.assertFalse(bibliotheque.retourner_livre("titre"))

if __name__ == "__main__":
    unittest.main()


