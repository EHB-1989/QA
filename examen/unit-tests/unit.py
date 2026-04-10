import unittest
from app import Livre, Bibliotheque

class TestLivre(unittest.TestCase):
  def setUp(self):
    self.livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")

  def test_emprunter(self):
    self.assertTrue(self.livre.emprunter())
    self.assertFalse(self.livre.emprunter())

  def test_retourner(self):
    self.livre.emprunter()
    self.assertTrue(self.livre.retourner())
    self.assertFalse(self.livre.retourner())

class TestBibliotheque(unittest.TestCase):
  def setUp(self):
    self.bibliotheque = Bibliotheque()
    self.livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")
    self.livre2 = Livre("1984", "George Orwell")
    self.bibliotheque.ajouter_livre(self.livre1)
    self.bibliotheque.ajouter_livre(self.livre2)

  def test_ajouter_livre(self):
    livre3 = Livre("Dune", "Frank Herbert")
    self.bibliotheque.ajouter_livre(livre3)
    self.assertIn(livre3, self.bibliotheque.livres)

  def test_emprunter_livre(self):
    self.assertTrue(self.bibliotheque.emprunter_livre("Le Petit Prince"))
    self.assertFalse(self.bibliotheque.emprunter_livre("Le Petit Prince"))
    self.assertFalse(self.bibliotheque.emprunter_livre("Livre Inexistant"))

  def test_retourner_livre(self):
    self.bibliotheque.emprunter_livre("Le Petit Prince")
    self.assertTrue(self.bibliotheque.retourner_livre("Le Petit Prince"))
    self.assertFalse(self.bibliotheque.retourner_livre("Livre Inexistant"))

if __name__ == '__main__':
  unittest.main()