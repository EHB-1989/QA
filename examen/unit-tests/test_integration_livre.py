from app import Livre, Bibliotheque
import unittest

class TestLivre(unittest.TestCase):
    def setUp(self):
        self.livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")

    def test_emprunter(self):
        self.assertTrue(self.livre.emprunter())

    def test_retourner(self):
        self.livre.emprunter()  
        self.assertTrue(self.livre.retourner())

class TestBibliotheque(unittest.TestCase):
    def setUp(self):
        self.bibliotheque = Bibliotheque()
        self.livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")
        self.bibliotheque.ajouter_livre(self.livre1)

    def test_ajouter_livre(self):
        self.assertEqual(len(self.bibliotheque.livres), 1)  

    def test_emprunter_livre(self):
        self.assertTrue(self.bibliotheque.emprunter_livre("Le Petit Prince"))

    def test_retourner_livre(self):
        self.bibliotheque.emprunter_livre("Le Petit Prince")
        self.assertTrue(self.bibliotheque.retourner_livre("Le Petit Prince"))

if __name__ == '__main__':
    unittest.main()
