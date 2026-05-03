import unittest
from app import Livre, Bibliotheque


class TestLivre(unittest.TestCase):

    def setUp(self):
        self.livre = Livre("1984", "George Orwell")

    def test_init(self):
        self.assertEqual(self.livre.titre, "1984")
        self.assertEqual(self.livre.auteur, "George Orwell")
        self.assertFalse(self.livre.est_emprunte)

    def test_emprunter_succes(self):
        result = self.livre.emprunter()
        self.assertTrue(result)
        self.assertTrue(self.livre.est_emprunte)

    def test_emprunter_deja_emprunte(self):
        self.livre.emprunter()
        result = self.livre.emprunter()
        self.assertFalse(result)
        self.assertTrue(self.livre.est_emprunte)

    def test_retourner_succes(self):
        self.livre.emprunter()
        result = self.livre.retourner()
        self.assertTrue(result)
        self.assertFalse(self.livre.est_emprunte)

    def test_retourner_non_emprunte(self):
        result = self.livre.retourner()
        self.assertFalse(result)
        self.assertFalse(self.livre.est_emprunte)


class TestBibliotheque(unittest.TestCase):

    def setUp(self):
        self.biblio = Bibliotheque()
        self.livre1 = Livre("1984", "George Orwell")
        self.livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")
        self.biblio.ajouter_livre(self.livre1)
        self.biblio.ajouter_livre(self.livre2)

    def test_ajouter_livre(self):
        livre3 = Livre("Les Misérables", "Victor Hugo")
        self.biblio.ajouter_livre(livre3)
        self.assertEqual(len(self.biblio.livres), 3)
        self.assertIn(livre3, self.biblio.livres)

    def test_emprunter_livre_succes(self):
        result = self.biblio.emprunter_livre("1984")
        self.assertTrue(result)
        self.assertTrue(self.livre1.est_emprunte)

    def test_emprunter_livre_inexistant(self):
        result = self.biblio.emprunter_livre("Livre Inexistant")
        self.assertFalse(result)

    def test_emprunter_livre_deja_emprunte(self):
        self.biblio.emprunter_livre("1984")
        result = self.biblio.emprunter_livre("1984")
        self.assertFalse(result)

    def test_retourner_livre_succes(self):
        self.biblio.emprunter_livre("1984")
        result = self.biblio.retourner_livre("1984")
        self.assertTrue(result)
        self.assertFalse(self.livre1.est_emprunte)

    def test_retourner_livre_non_emprunte(self):
        result = self.biblio.retourner_livre("1984")
        self.assertFalse(result)

    def test_retourner_livre_inexistant(self):
        result = self.biblio.retourner_livre("Livre Inexistant")
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
