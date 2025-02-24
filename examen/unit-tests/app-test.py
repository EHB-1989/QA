import unittest
from app import Livre, Bibliotheque

class TestLivre(unittest.TestCase):
  def setUp(self):
    self.livre = Livre('La maison des feuilles', 'Mark Z. Danielewski')

  def test_proprietes_livre(self):
    self.assertEqual(self.livre.titre, 'La maison des feuilles')
    self.assertEqual(self.livre.auteur, 'Mark Z. Danielewski')
    self.assertFalse(self.livre.est_emprunte)

  def test_emprunt_livre(self):
    self.assertTrue(self.livre.emprunter())
    self.assertTrue(self.livre.est_emprunte)

    # Un double emprunt doit être impossible.
    self.assertFalse(self.livre.emprunter())

  def test_retour_livre(self):
    self.livre.emprunter()
    self.assertTrue(self.livre.retourner())
    self.assertFalse(self.livre.est_emprunte)

    # Un double retour doit être impossible
    self.assertFalse(self.livre.retourner())

class TestBibliotheque(unittest.TestCase):
  def setUp(self):
    self.bibliotheque = Bibliotheque()
    self.livre = Livre('La ferme des animaux', 'George Orwell')

  def test_proprietes_bibliotheque(self):
    self.assertEqual(len(self.bibliotheque.livres), 0)

  def test_ajouter_livre(self):
    self.bibliotheque.ajouter_livre(self.livre)
    self.assertEqual(len(self.bibliotheque.livres), 1)
    self.assertEqual(self.bibliotheque.livres[0].titre, 'La ferme des animaux')

  def test_emprunter_livre(self):
    self.bibliotheque.ajouter_livre(self.livre)
    self.assertTrue(self.bibliotheque.emprunter_livre('La ferme des animaux'))
    self.assertTrue(self.livre.est_emprunte)

    # Un double emprunt doit être impossible.
    self.assertFalse(self.bibliotheque.emprunter_livre('La ferme des animaux'))

  def test_retourner_livre(self):
    self.bibliotheque.ajouter_livre(self.livre)
    self.livre.emprunter()
    self.assertTrue(self.bibliotheque.retourner_livre('La ferme des animaux'))
    self.assertFalse(self.livre.est_emprunte)

    # Un double retour doit être impossible
    self.assertFalse(self.bibliotheque.retourner_livre('La ferme des animaux'))

if __name__ == '__main__':
  unittest.main()