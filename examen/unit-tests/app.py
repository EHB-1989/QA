import unittest

class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        self.est_emprunte = False

    def emprunter(self):
        if self.est_emprunte:
            return False
        else:
            self.est_emprunte = True
            return True

    def retourner(self):
        if self.est_emprunte:
            self.est_emprunte = False
            return True
        else:
            return False

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def emprunter_livre(self, titre):
        for livre in self.livres:
            if livre.titre == titre and not livre.est_emprunte:
                livre.emprunter()
                return True
        return False

    def retourner_livre(self, titre):
        for livre in self.livres:
            if livre.titre == titre and livre.est_emprunte:
                livre.retourner()
                return True
        return False

class TestBibliotheque(unittest.TestCase):
    def setUp(self):
        self.bibliotheque = Bibliotheque()
        self.livre1 = Livre("Le livre officiel", "Auteur Dulivre")
        self.livre2 = Livre("Livre des sciences", "Auteur Scienti")
        self.bibliotheque.ajouter_livre(self.livre1)
        self.bibliotheque.ajouter_livre(self.livre2)

    def test_ajouter_livre(self):
        self.assertIn(self.livre1, self.bibliotheque.livres)
        self.assertIn(self.livre2, self.bibliotheque.livres)

    def test_emprunter_livre_disponible(self):
        resultat = self.bibliotheque.emprunter_livre("Le livre officiel")
        self.assertTrue(resultat)
        self.assertTrue(self.livre1.est_emprunte)

    def test_emprunter_livre_deja_emprunte(self):
        self.bibliotheque.emprunter_livre("Le livre officiel")
        resultat = self.bibliotheque.emprunter_livre("Le livre officiel")
        self.assertFalse(resultat)

    def test_emprunter_livre_inexistant(self):
        resultat = self.bibliotheque.emprunter_livre("Inconnu")
        self.assertFalse(resultat)

    def test_retourner_livre_emprunte(self):
        self.bibliotheque.emprunter_livre("Livre des sciences")
        resultat = self.bibliotheque.retourner_livre("Livre des sciences")
        self.assertTrue(resultat)
        self.assertFalse(self.livre2.est_emprunte)

    def test_retourner_livre_non_emprunte(self):
        resultat = self.bibliotheque.retourner_livre("Le livre officiel")
        self.assertFalse(resultat)

    def test_retourner_livre_inexistant(self):
        resultat = self.bibliotheque.retourner_livre("Inconnu")
        self.assertFalse(resultat)

if __name__ == '__main__':
    unittest.main()