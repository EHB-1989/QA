import unittest
from app import Livre, Bibliotheque


class TestLivre(unittest.TestCase):

    def setUp(self):
        self.livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")

    def test_creation_livre(self):
        self.assertEqual(self.livre.titre, "Le Petit Prince")
        self.assertEqual(self.livre.auteur, "Antoine de Saint-Exupéry")
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
        self.livre2 = Livre("Dune", "Frank Herbert")

    def test_ajouter_livre(self):
        self.bibliotheque.ajouter_livre(self.livre1)
        self.assertIn(self.livre1, self.bibliotheque.livres)
        self.assertEqual(len(self.bibliotheque.livres), 1)

    def test_ajouter_plusieurs_livres(self):
        self.bibliotheque.ajouter_livre(self.livre1)
        self.bibliotheque.ajouter_livre(self.livre2)
        self.assertEqual(len(self.bibliotheque.livres), 2)

    def test_emprunter_livre_existant(self):
        self.bibliotheque.ajouter_livre(self.livre1)
        resultat = self.bibliotheque.emprunter_livre("1984")
        self.assertTrue(resultat)
        self.assertTrue(self.livre1.est_emprunte)

    def test_emprunter_livre_inexistant(self):
        self.bibliotheque.ajouter_livre(self.livre1)
        resultat = self.bibliotheque.emprunter_livre("Titre Inconnu")
        self.assertFalse(resultat)

    def test_emprunter_livre_deja_emprunte(self):
        self.bibliotheque.ajouter_livre(self.livre1)
        self.bibliotheque.emprunter_livre("1984")
        resultat = self.bibliotheque.emprunter_livre("1984")
        self.assertFalse(resultat)

    def test_retourner_livre_emprunte(self):
        self.bibliotheque.ajouter_livre(self.livre1)
        self.bibliotheque.emprunter_livre("1984")
        resultat = self.bibliotheque.retourner_livre("1984")
        self.assertTrue(resultat)
        self.assertFalse(self.livre1.est_emprunte)

    def test_retourner_livre_non_emprunte(self):
        self.bibliotheque.ajouter_livre(self.livre1)
        resultat = self.bibliotheque.retourner_livre("1984")
        self.assertFalse(resultat)

    def test_retourner_livre_inexistant(self):
        self.bibliotheque.ajouter_livre(self.livre1)
        resultat = self.bibliotheque.retourner_livre("Titre Inconnu")
        self.assertFalse(resultat)

    def test_bibliotheque_initialement_vide(self):
        self.assertEqual(len(self.bibliotheque.livres), 0)


if __name__ == "__main__":
    unittest.main()
