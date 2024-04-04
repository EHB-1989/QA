import unittest
from app import Livre, Bibliotheque

class TestBiblio(unittest.TestCase):
    def setUp(self):
        self.biblio = Bibliotheque()
        self.livre = Livre("Le temps des tempêtes", "Sarkozy")
        self.livre2 = Livre("Le temps des combats", "Sarkozy")
        self.livre2.est_emprunte = True
    
    def test_ajouter_livre(self):
        self.assertEqual(self.biblio.livres, [])
        self.biblio.ajouter_livre(self.livre)
        self.biblio.ajouter_livre(self.livre2)
        self.assertEqual(self.biblio.livres, [self.livre, self.livre2])

    def test_emprunter_livre(self):
        self.biblio.ajouter_livre(self.livre)
        self.biblio.ajouter_livre(self.livre2)
        self.assertEqual(self.biblio.emprunter_livre(self.livre.titre), True)
        self.assertEqual(self.biblio.emprunter_livre(self.livre2.titre), False)

    def test_retourner_livre(self):
        self.biblio.ajouter_livre(self.livre)
        self.biblio.ajouter_livre(self.livre2)
        self.assertEqual(self.biblio.retourner_livre(self.livre.titre), False)
        self.assertEqual(self.biblio.retourner_livre(self.livre2.titre), True)

    def test_emprunter(self):
        self.assertEqual(self.livre.emprunter(), True)
        self.assertEqual(self.livre2.emprunter(), False)

    def test_retourner(self):
        self.assertEqual(self.livre.retourner(), False)
        self.assertEqual(self.livre2.retourner(), True)

if __name__ == '__main__':
    unittest.main()