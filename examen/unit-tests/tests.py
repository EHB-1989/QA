import unittest
from app import Livre,Bibliotheque


class TestLivre(unittest.TestCase):
    livre = Livre("Naruto", "Masashi Kishimoto")

    def test_emprunter(self):
        self.assertTrue(self.livre.emprunter())
        self.assertTrue(self.livre.est_emprunte)

    def test_retourner(self):
        self.livre.emprunter()
        self.assertTrue(self.livre.retourner())
        self.assertFalse(self.livre.est_emprunte)

class TestBibliotheque(unittest.TestCase):
    bibliotheque = Bibliotheque()
    livre1 = Livre("Naruto", "Masashi Kishimoto")
    livre2 = Livre("One Piece", "Eiichirō Oda")
    bibliotheque.ajouter_livre(livre1)
    bibliotheque.ajouter_livre(livre2)

    def test_ajouter_livre(self):
        self.assertEqual(len(self.bibliotheque.livres), 2)

    def test_emprunter_livre(self):
        self.assertTrue(self.bibliotheque.emprunter_livre("Naruto"))
        self.assertTrue(self.livre1.est_emprunte)

    def test_retourner_livre(self):
        self.bibliotheque.emprunter_livre("Naruto")
        self.assertTrue(self.bibliotheque.retourner_livre("Naruto"))
        self.assertFalse(self.livre1.est_emprunte)

    def test_emprunter_livre_inexistant(self):
        self.assertFalse(self.bibliotheque.emprunter_livre("Bleach"))

    def test_retourner_livre_non_emprunte(self):
        self.assertFalse(self.bibliotheque.retourner_livre("Bleach"))

if __name__ == '__main__':
    unittest.main()
