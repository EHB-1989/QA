import unittest
from app import Livre, Bibliotheque

class TestLivre(unittest.TestCase):
    def test_emprunter_livre(self):
        livre = Livre("Jujutsu Kaisen", "Gege Akutami")
        self.assertFalse(livre.est_emprunte)
        livre.emprunter()
        self.assertTrue(livre.est_emprunte)

    def test_retourner_livre(self):
        livre = Livre("My Hero Academia", "Kōhei Horikoshi")
        livre.emprunter()
        self.assertTrue(livre.est_emprunte)
        livre.retourner()
        self.assertFalse(livre.est_emprunte)

class TestBibliotheque(unittest.TestCase):
    def test_ajouter_livre(self):
        biblio = Bibliotheque()
        livre = Livre("One Piece", "Eiichirō Oda")
        biblio.ajouter_livre(livre)
        self.assertIn(livre, biblio.livres)

    def test_emprunter_livre(self):
        biblio = Bibliotheque()
        livre = Livre("Naruto", "Masashi Kishimoto")
        biblio.ajouter_livre(livre)
        self.assertTrue(biblio.emprunter_livre("Naruto"))
        self.assertFalse(biblio.emprunter_livre("pas existant"))

    def test_retourner_livre(self):
        biblio = Bibliotheque()
        livre = Livre("Chainsaw Man", "Tatsuki Fujimoto")
        biblio.ajouter_livre(livre)
        biblio.emprunter_livre("Harry Potter")
        self.assertTrue(biblio.retourner_livre("Harry Potter"))
        self.assertFalse(biblio.retourner_livre("pas existant"))

if __name__ == '__main__':
    unittest.main()