import unittest
from app import Livre
from app import Bibliotheque

class TestLivre(unittest.TestCase):

    def Initialisation(self):
        self.livre = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien")

    def test_emprunter(self):
        self.assertTrue(self.livre.emprunter())
        self.assertFalse(self.livre.emprunter())

    def test_retourner(self):
        self.livre.emprunter()
        self.assertTrue(self.livre.retourner())
        self.assertFalse(self.livre.retourner())

class TestBibliotheque(unittest.TestCase):

    def Initialisation(self):
        self.bibliotheque = Bibliotheque()
        self.livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")
        self.livre2 = Livre("1984", "George Orwell")
        self.livre3 = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien")
        self.bibliotheque.ajouter_livre(self.livre1)
        self.bibliotheque.ajouter_livre(self.livre2)
        self.bibliotheque.ajouter_livre(self.livre3)

    def test_ajouter_livre(self):
        self.assertEqual(len(self.bibliotheque.livres), 3)

    def test_emprunter_livre(self):
        self.assertTrue(self.bibliotheque.emprunter_livre("Le Petit Prince"))
        self.assertFalse(self.bibliotheque.emprunter_livre("Le Petit Prince"))
        self.assertTrue(self.bibliotheque.emprunter_livre("1984"))
        self.assertTrue(self.bibliotheque.emprunter_livre("Le Seigneur des Anneaux"))
    
    def test_emprunter_livre_inexistant(self):
        self.assertFalse(self.bibliotheque.emprunter_livre("La maison des feuilles"))

    def test_retourner_livre(self):
        self.bibliotheque.emprunter_livre("Le Petit Prince")
        self.assertTrue(self.bibliotheque.retourner_livre("Le Petit Prince"))
        self.assertFalse(self.bibliotheque.retourner_livre("Le Seigneur des Anneaux"))
        
        

if __name__ == '__main__':
    unittest.main()
