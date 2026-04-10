import unittest
from app import Livre, Bibliotheque


# Tests unitaires pour la classe Livre
class TestLivre(unittest.TestCase):

    def setUp(self):
        # On crée un livre de test avant chaque test
        self.livre = Livre("Python Avancé", "Guido Van Rossum")

    def test_creation_livre(self):
        # Un livre créé doit avoir les bons attributs et ne pas être emprunté
        self.assertEqual(self.livre.titre, "Python Avancé")
        self.assertEqual(self.livre.auteur, "Guido Van Rossum")
        self.assertFalse(self.livre.est_emprunte)

    def test_emprunter_livre_disponible(self):
        # On peut emprunter un livre qui est disponible
        resultat = self.livre.emprunter()
        self.assertTrue(resultat)
        self.assertTrue(self.livre.est_emprunte)

    def test_emprunter_livre_deja_emprunte(self):
        # On ne peut pas emprunter un livre déjà emprunté
        self.livre.emprunter()
        resultat = self.livre.emprunter()
        self.assertFalse(resultat)
        self.assertTrue(self.livre.est_emprunte)

    def test_retourner_livre_emprunte(self):
        # Retourner un livre emprunté doit le rendre disponible
        self.livre.emprunter()
        resultat = self.livre.retourner()
        self.assertTrue(resultat)
        self.assertFalse(self.livre.est_emprunte)

    def test_retourner_livre_non_emprunte(self):
        # On ne peut pas retourner un livre qui n'a pas été emprunté
        resultat = self.livre.retourner()
        self.assertFalse(resultat)
        self.assertFalse(self.livre.est_emprunte)


# Tests unitaires pour la classe Bibliotheque
class TestBibliotheque(unittest.TestCase):

    def setUp(self):
        # On prépare une bibliothèque avec 2 livres avant chaque test
        self.bibliotheque = Bibliotheque()
        self.livre1 = Livre("Clean Code", "Robert Martin")
        self.livre2 = Livre("Design Patterns", "Gang of Four")
        self.bibliotheque.ajouter_livre(self.livre1)
        self.bibliotheque.ajouter_livre(self.livre2)

    def test_ajouter_livre(self):
        # Ajouter un livre doit l'inclure dans la liste
        nouveau_livre = Livre("Le Petit Prince", "Saint-Exupéry")
        self.bibliotheque.ajouter_livre(nouveau_livre)
        self.assertIn(nouveau_livre, self.bibliotheque.livres)
        self.assertEqual(len(self.bibliotheque.livres), 3)

    def test_emprunter_livre_existant(self):
        # Emprunter un livre disponible doit réussir
        resultat = self.bibliotheque.emprunter_livre("Clean Code")
        self.assertTrue(resultat)
        self.assertTrue(self.livre1.est_emprunte)

    def test_emprunter_livre_inexistant(self):
        # Emprunter un livre qui n'existe pas doit échouer
        resultat = self.bibliotheque.emprunter_livre("Livre Inexistant")
        self.assertFalse(resultat)

    def test_emprunter_livre_deja_emprunte(self):
        # Emprunter deux fois le même livre doit échouer la 2ème fois
        self.bibliotheque.emprunter_livre("Clean Code")
        resultat = self.bibliotheque.emprunter_livre("Clean Code")
        self.assertFalse(resultat)

    def test_retourner_livre_emprunte(self):
        # Retourner un livre emprunté doit le remettre disponible
        self.bibliotheque.emprunter_livre("Design Patterns")
        resultat = self.bibliotheque.retourner_livre("Design Patterns")
        self.assertTrue(resultat)
        self.assertFalse(self.livre2.est_emprunte)

    def test_retourner_livre_non_emprunte(self):
        # Retourner un livre qui n'est pas emprunté doit échouer
        resultat = self.bibliotheque.retourner_livre("Clean Code")
        self.assertFalse(resultat)

    def test_retourner_livre_inexistant(self):
        # Retourner un livre qui n'existe pas doit échouer
        resultat = self.bibliotheque.retourner_livre("Livre Inexistant")
        self.assertFalse(resultat)

    def test_bibliotheque_initialement_vide(self):
        # Une nouvelle bibliothèque ne contient aucun livre
        nouvelle_biblio = Bibliotheque()
        self.assertEqual(len(nouvelle_biblio.livres), 0)


if __name__ == "__main__":
    unittest.main()
