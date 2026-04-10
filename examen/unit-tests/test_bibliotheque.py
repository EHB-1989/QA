import unittest
from app import Livre, Bibliotheque

class TestBibliotheque(unittest.TestCase):

    def setUp(self):
        self.biblio = Bibliotheque()
        self.livre = Livre("Harry Potter", "J.K Rowling")

    def test_ajouter_livre(self):
        self.biblio.ajouter_livre(self.livre)
        self.assertIn(self.livre, self.biblio.livres)

    def test_emprunter_livre(self):
        self.biblio.ajouter_livre(self.livre)
        self.biblio.emprunter_livre(self.livre.titre)
        self.assertTrue(self.livre.est_emprunte)

    def test_retour_livre(self):
        self.biblio.ajouter_livre(self.livre)
        self.biblio.emprunter_livre(self.livre.titre)
        self.biblio.retourner_livre(self.livre.titre)
        self.assertFalse(self.livre.est_emprunte)

if __name__ == '__main__':
    unittest.main()
