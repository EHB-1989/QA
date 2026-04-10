import unittest
from app import Livre, Bibliotheque

class TestLivre(unittest.TestCase):
    def setUp(self):
        self.livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")

    def test_initialisation(self):
        self.assertEqual(self.livre.titre, "Le Petit Prince")
        self.assertEqual(self.livre.auteur, "Antoine de Saint-Exupéry")
        self.assertFalse(self.livre.est_emprunte)

    def test_emprunter_succes(self):
        self.assertTrue(self.livre.emprunter())
        self.assertTrue(self.livre.est_emprunte)

    def test_emprunter_deja_emprunte(self):
        self.livre.emprunter() # Premier emprunt
        self.assertFalse(self.livre.emprunter()) # Deuxième tentative

    def test_retourner_succes(self):
        self.livre.emprunter()
        self.assertTrue(self.livre.retourner())
        self.assertFalse(self.livre.est_emprunte)

    def test_retourner_non_emprunte(self):
        self.assertFalse(self.livre.retourner())

class TestBibliotheque(unittest.TestCase):
    def setUp(self):
        self.biblio = Bibliotheque()
        self.livre1 = Livre("1984", "George Orwell")
        self.livre2 = Livre("Fahrenheit 451", "Ray Bradbury")

    def test_ajouter_livre(self):
        self.biblio.ajouter_livre(self.livre1)
        self.assertEqual(len(self.biblio.livres), 1)
        self.assertIn(self.livre1, self.biblio.livres)
        
        self.biblio.ajouter_livre(self.livre2)
        self.assertEqual(len(self.biblio.livres), 2)

    def test_emprunter_livre_succes(self):
        self.biblio.ajouter_livre(self.livre1)
        resultat = self.biblio.emprunter_livre("1984")
        self.assertTrue(resultat)
        self.assertTrue(self.livre1.est_emprunte)

    def test_emprunter_livre_inexistant(self):
        resultat = self.biblio.emprunter_livre("Inconnu")
        self.assertFalse(resultat)

    def test_emprunter_livre_deja_emprunte(self):
        self.biblio.ajouter_livre(self.livre1)
        self.biblio.emprunter_livre("1984")
        resultat = self.biblio.emprunter_livre("1984") # Deuxième tentative
        self.assertFalse(resultat)

    def test_retourner_livre_succes(self):
        self.biblio.ajouter_livre(self.livre1)
        self.biblio.emprunter_livre("1984")
        resultat = self.biblio.retourner_livre("1984")
        self.assertTrue(resultat)
        self.assertFalse(self.livre1.est_emprunte)

    def test_retourner_livre_non_emprunte(self):
        self.biblio.ajouter_livre(self.livre1)
        resultat = self.biblio.retourner_livre("1984")
        self.assertFalse(resultat)

    def test_retourner_livre_inexistant(self):
        resultat = self.biblio.retourner_livre("Inconnu")
        self.assertFalse(resultat)

if __name__ == '__main__':
    unittest.main()
