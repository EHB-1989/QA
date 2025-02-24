import unittest
from app import Livre, Bibliotheque

class TestLivre(unittest.TestCase):

    def test_livre_emprunter(self):
        livre = Livre("One Piece", "Eichiro Oda")
        self.assertTrue(livre.emprunter())
        self.assertFalse(livre.emprunter())

    def test_livre_retourner(self):
        livre = Livre("One Piece", "Eichiro Oda")
        livre.emprunter()
        self.assertTrue(livre.retourner())
        self.assertFalse(livre.retourner())

class TestBibliotheque(unittest.TestCase):

    def setUp(self):
        self.biblio = Bibliotheque()

    def test_bibliotheque_ajouter_livre(self):
        livre = Livre("One Piece", "Eichiro Oda")
        self.biblio.ajouter_livre(livre)
        self.assertEqual(len(self.biblio.livres), 1)

    def test_bibliotheque_emprunter_livre(self):
        livre = Livre("One Piece", "Eichiro Oda")
        self.biblio.ajouter_livre(livre)
        self.assertTrue(self.biblio.emprunter_livre("One Piece"))
        self.assertFalse(self.biblio.emprunter_livre("One Piece"))

    def test_bibliotheque_retourner_livre(self):
        livre = Livre("One Piece", "Eichiro Oda")
        self.biblio.ajouter_livre(livre)
        self.biblio.emprunter_livre("One Piece")
        self.assertTrue(self.biblio.retourner_livre("One Piece"))
        self.assertFalse(self.biblio.retourner_livre("One Piece"))

if __name__ == '__main__':
    unittest.main()