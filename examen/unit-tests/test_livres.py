import unittest
from app import Livre, Bibliotheque

class TestBibliotheque(unittest.TestCase):
    def setUp(self):
        """Initialisation avant chaque test"""
        self.biblio = Bibliotheque()
        self.livre1 = Livre("One Piece", "Eiichirō Oda")
        self.livre2 = Livre("Dragon Ball", "Akira Toriyama")
        self.biblio.ajouter_livre(self.livre1)
        self.biblio.ajouter_livre(self.livre2)

    def test_ajouter_livre(self):
        livre3 = Livre("Naruto", "Masashi Kishimoto")
        self.biblio.ajouter_livre(livre3)
        self.assertIn(livre3, self.biblio.livres)

    def test_emprunter_livre_succes(self):
        self.assertTrue(self.biblio.emprunter_livre("One Piece"))
        self.assertTrue(self.livre1.est_emprunte)

    def test_emprunter_livre_deja_emprunte(self):
        self.biblio.emprunter_livre("One Piece")  
        self.assertFalse(self.biblio.emprunter_livre("One Piece"))  # Normaly, it should return False because the book is already borrowed

    def test_retourner_livre_succes(self):
        self.biblio.emprunter_livre("One Piece")
        self.assertTrue(self.biblio.retourner_livre("One Piece"))
        self.assertFalse(self.livre1.est_emprunte)

    def test_retourner_livre_non_emprunte(self):
        self.assertFalse(self.biblio.retourner_livre("One Piece"))

if __name__ == '__main__':
    unittest.main()
