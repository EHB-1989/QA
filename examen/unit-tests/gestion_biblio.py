import unittest
from app import Livre, Bibliotheque

class TestGestionBibliotheque(unittest.TestCase):

    def test_ajouter_livre(self):
        bibliotheque = Bibliotheque()
        livre = Livre("Le Petit Prince", "Antoine")
        bibliotheque.ajouter_livre(livre)
        self.assertIn(livre, bibliotheque.livres)

    def test_emprunter_livre_disponible(self):
        bibliotheque = Bibliotheque()
        livre = Livre("1984", "Hamid")
        bibliotheque.ajouter_livre(livre)
        resultat = bibliotheque.emprunter_livre("1984")
        self.assertTrue(resultat)
        self.assertTrue(livre.est_emprunte)

    def test_emprunter_livre_non_disponible(self):
        bibliotheque = Bibliotheque()
        livre = Livre("1984", "George")
        livre.emprunter()  
        bibliotheque.ajouter_livre(livre)
        resultat = bibliotheque.emprunter_livre("1984")
        self.assertFalse(resultat)

    def test_retourner_livre(self):
        bibliotheque = Bibliotheque()
        livre = Livre("Les Misérables", "Hugo")
        bibliotheque.ajouter_livre(livre)
        livre.emprunter() 
        resultat = bibliotheque.retourner_livre("Les Misérables")
        self.assertTrue(resultat)
        self.assertFalse(livre.est_emprunte)

# Le livre n'était pas emprunte il ne peut pas être retourne
    def test_retourner_livre_non_emprunte(self):
        bibliotheque = Bibliotheque()
        livre = Livre("Les Misérables", "Victor Hugo")
        bibliotheque.ajouter_livre(livre)
        resultat = bibliotheque.retourner_livre("Les Misérables")
        self.assertFalse(resultat)  

if __name__ == '__main__':
    unittest.main()
