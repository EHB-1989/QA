import unittest
from app import Livre, Bibliotheque  # Remplacez 'votre_module' par le nom de votre fichier Python

class TestLivre(unittest.TestCase):
    def test_creation_livre(self):
        livre = Livre("1984", "George Orwell")
        self.assertEqual(livre.titre, "1984")
        self.assertEqual(livre.auteur, "George Orwell")
        self.assertFalse(livre.est_emprunte)
    
    def test_emprunter_livre_succes(self):
        livre = Livre("1984", "George Orwell")
        self.assertTrue(livre.emprunter())  # Premier emprunt réussi
    
    def test_emprunter_livre_echec(self):
        livre = Livre("1984", "George Orwell")
        livre.emprunter()
        self.assertFalse(livre.emprunter())  # Ne peut pas emprunter deux fois
    
    def test_retourner_livre_succes(self):
        livre = Livre("1984", "George Orwell")
        livre.emprunter()
        self.assertTrue(livre.retourner())  # Retour réussi
    
    def test_retourner_livre_echec(self):
        livre = Livre("1984", "George Orwell")
        self.assertFalse(livre.retourner())  # Ne peut pas retourner un livre non emprunté

class TestBibliotheque(unittest.TestCase):
    def test_ajouter_livre(self):
        biblio = Bibliotheque()
        livre = Livre("1984", "George Orwell")
        biblio.ajouter_livre(livre)
        self.assertIn(livre, biblio.livres)
    
    def test_emprunter_livre_succes(self):
        biblio = Bibliotheque()
        livre = Livre("1984", "George Orwell")
        biblio.ajouter_livre(livre)
        self.assertTrue(biblio.emprunter_livre("1984"))
    
    def test_emprunter_livre_echec(self):
        biblio = Bibliotheque()
        livre = Livre("1984", "George Orwell")
        biblio.ajouter_livre(livre)
        biblio.emprunter_livre("1984")  # Déjà emprunté
        self.assertFalse(biblio.emprunter_livre("1984"))
        self.assertFalse(biblio.emprunter_livre("Le Petit Prince"))  # Livre inexistant
    
    def test_retourner_livre_succes(self):
        biblio = Bibliotheque()
        livre = Livre("1984", "George Orwell")
        biblio.ajouter_livre(livre)
        biblio.emprunter_livre("1984")
        self.assertTrue(biblio.retourner_livre("1984"))
    
    def test_retourner_livre_echec(self):
        biblio = Bibliotheque()
        livre = Livre("1984", "George Orwell")
        biblio.ajouter_livre(livre)
        self.assertFalse(biblio.retourner_livre("1984"))  # Pas encore emprunté
        self.assertFalse(biblio.retourner_livre("Le Petit Prince"))  # Livre inexistant

if __name__ == "__main__":
    unittest.main()