import unittest

from app import Livre
from app import Bibliotheque

class TestBibliotheque(unittest.TestCase):
    def test_ajout_livre(self):
        l = Livre("Titre", "Auteur")
    
        b = Bibliotheque()
        b.ajouter_livre(l)
        self.assertEqual(b.livres.index(l), 0)

    def test_emprunt_livre_bibliotheque(self):
        titre = "Eragon"
        l = Livre(titre, "Auteur")
        b = Bibliotheque()
        b.ajouter_livre(l)
        b.emprunter_livre(titre)

        self.assertFalse(l.emprunter())
        #self.assertTrue(l.est_emprunte)
        self.assertFalse(b.emprunter_livre(titre))
    
    def test_retourner_livre_blibliotheque(self):
        titre = "Eragon"
        l = Livre(titre, "Auteur")
        b = Bibliotheque()
        b.ajouter_livre(l)
        b.emprunter_livre(titre)

        self.assertTrue(l.est_emprunte)

        b.retourner_livre(titre)

        #self.assertFalse(l.est_emprunte)
        self.assertFalse(b.retourner_livre(titre))
        self.assertTrue(l.emprunter())

    def test_livre(self):
        l = Livre("Titre", "Auteur")

        l.emprunter()

        self.assertTrue(l.est_emprunte)
        self.assertFalse(l.emprunter())
        
        l.retourner()

        self.assertFalse(l.est_emprunte)
        self.assertTrue(l.emprunter())
        





if __name__ == '__main__':
    unittest.main()