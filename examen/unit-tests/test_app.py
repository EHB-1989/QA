import unittest
from app import Livre, Bibliotheque

class TestLivre(unittest.TestCase):
    def setUp(self):
        self.livre = Livre("1984", "George Orwell")

    def test_creation_livre(self):
        self.assertEqual(self.livre.titre, "1984") 
        self.assertEqual(self.livre.auteur, "George Orwell")  # Meilleur auteur :) Selon aminata
        self.assertFalse(self.livre.est_emprunte)

    def test_emprunter_livre_disponible(self):
        resultat = self.livre.emprunter()
        self.assertTrue(resultat)
        self.assertTrue(self.livre.est_emprunte)

    def test_emprunter_livre_deja_emprunte(self):
        self.livre.emprunter()
        resultat = self.livre.emprunter()
        self.assertFalse(resultat)
        self.assertTrue(self.livre.est_emprunte)

    def test_retourner_livre_emprunte(self):
        self.livre.emprunter()
        resultat = self.livre.retourner()
        self.assertTrue(resultat)
        self.assertFalse(self.livre.est_emprunte)

    def test_retourner_livre_non_emprunte(self):
        resultat = self.livre.retourner()
        self.assertFalse(resultat)
        self.assertFalse(self.livre.est_emprunte)


class TestBibliotheque(unittest.TestCase):
    def setUp(self):
        self.bibliotheque = Bibliotheque()
        self.livre1 = Livre("1984", "George Orwell")
        self.livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")
        self.bibliotheque.ajouter_livre(self.livre1)
        self.bibliotheque.ajouter_livre(self.livre2)

    def test_ajouter_livre(self):
        livre3 = Livre("Dune", "Frank Herbert")
        self.bibliotheque.ajouter_livre(livre3)
        self.assertEqual(len(self.bibliotheque.livres), 3)
        self.assertIs(self.bibliotheque.livres[-1], livre3)

    def test_emprunter_livre_existant(self):
        resultat = self.bibliotheque.emprunter_livre("1984")
        self.assertTrue(resultat)
        self.assertTrue(self.livre1.est_emprunte)

    def test_emprunter_livre_introuvable(self):
        resultat = self.bibliotheque.emprunter_livre("Livre inconnu")
        self.assertFalse(resultat)

    def test_emprunter_livre_deja_emprunte(self):
        self.bibliotheque.emprunter_livre("1984")
        resultat = self.bibliotheque.emprunter_livre("1984")
        self.assertFalse(resultat)

    def test_retourner_livre_emprunte(self):
        self.bibliotheque.emprunter_livre("1984")
        resultat = self.bibliotheque.retourner_livre("1984")
        self.assertTrue(resultat)
        self.assertFalse(self.livre1.est_emprunte)

    def test_retourner_livre_non_emprunte(self):
        resultat = self.bibliotheque.retourner_livre("Le Petit Prince")
        self.assertFalse(resultat)

    def test_retourner_livre_introuvable(self):
        resultat = self.bibliotheque.retourner_livre("Livre inconnu")
        self.assertFalse(resultat)


if __name__ == "__main__":
    unittest.main()
