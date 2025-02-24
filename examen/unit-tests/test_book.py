import unittest
from app import Livre, Bibliotheque

class TestBibliotheque(unittest.TestCase):
    def setUp(self):
        """Initning the test environment."""
        self.biblio = Bibliotheque()
        self.livre1 = Livre("One Piece", "Eiichirō Oda")
        self.livre2 = Livre("Dragon Ball", "Akira Toriyama")
        self.biblio.ajouter_livre(self.livre1)
        self.biblio.ajouter_livre(self.livre2)

    def test_add_book(self):
        livre3 = Livre("Naruto", "Masashi Kishimoto")
        self.biblio.ajouter_livre(livre3)
        self.assertIn(livre3, self.biblio.livres)

    def test_borrow_book_success(self):
        self.assertTrue(self.biblio.emprunter_livre("One Piece"))
        self.assertTrue(self.livre1.est_emprunte)

    def test_borrow_book_already_borrowed(self):
        self.biblio.emprunter_livre("One Piece")  
        self.assertFalse(self.biblio.emprunter_livre("One Piece"))  # Normaly, it should return False because the book is already borrowed

    def test_return_book_success(self):
        self.biblio.emprunter_livre("One Piece")
        self.assertTrue(self.biblio.retourner_livre("One Piece"))
        self.assertFalse(self.livre1.est_emprunte)

    def test_return_book_not_borrowed(self):
        self.assertFalse(self.biblio.retourner_livre("One Piece"))

if __name__ == '__main__':
    unittest.main()
