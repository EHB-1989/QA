"""
------------------------------------------------------------
 Nom du fichier : unit_test_hugo.py
 Auteur        : Moulard Hugo
 Date          : 24/02/2025
 Description   : Tests unitaires sur Bibliothèque et Livre
------------------------------------------------------------
"""

import unittest
from app import Bibliotheque, Livre

class TestBibliotheque(unittest.TestCase):
    def setUp(self):
        self.biblio = Bibliotheque()
        self.livre1 = Livre("1984", "George Orwell")
        self.livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")
        self.biblio.ajouter_livre(self.livre1)
        self.biblio.ajouter_livre(self.livre2)
    
    def test_ajouter_livre(self):
        self.assertIn(self.livre1, self.biblio.livres)
        self.assertIn(self.livre2, self.biblio.livres)

    def test_emprunter_livre_disponible(self):
        self.assertTrue(self.biblio.emprunter_livre("1984"))
        self.assertTrue(self.livre1.est_emprunte)
    
    def test_emprunter_livre_deja_emprunte(self):
        self.biblio.emprunter_livre("1984")
        self.assertFalse(self.biblio.emprunter_livre("1984"))
    
    def test_emprunter_livre_inexistant(self):
        self.assertFalse(self.biblio.emprunter_livre("Inconnu"))
    
    def test_retourner_livre_emprunte(self):
        self.biblio.emprunter_livre("1984")
        self.assertTrue(self.biblio.retourner_livre("1984"))
        self.assertFalse(self.livre1.est_emprunte)
    
    def test_retourner_livre_non_emprunte(self):
        self.assertFalse(self.biblio.retourner_livre("1984"))
    
    def test_retourner_livre_inexistant(self):
        self.assertFalse(self.biblio.retourner_livre("Inconnu"))
    
    def test_livre_emprunter_deja_emprunte(self):
        self.assertTrue(self.livre1.emprunter())
        self.assertFalse(self.livre1.emprunter())
    
    def test_livre_retourner_non_emprunte(self):
        self.assertFalse(self.livre1.retourner())
    
    def test_livre_retourner_apres_emprunt(self):
        self.livre1.emprunter()
        self.assertTrue(self.livre1.retourner())
        self.assertFalse(self.livre1.est_emprunte)

if __name__ == "__main__":
    unittest.main()