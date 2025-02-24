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

class TestLivre(unittest.TestCase):
    def setUp(self):
        self.livre = Livre("Harry Potter", "J.K. Rowling")

    def test_initialisation(self):
        self.assertEqual(self.livre.titre, "Harry Potter")
        self.assertEqual(self.livre.auteur, "J.K. Rowling")
        self.assertFalse(self.livre.est_emprunte)

    def test_emprunter(self):
        # Le livre n'est pas emprunté au départ, l'emprunt doit réussir.
        self.assertTrue(self.livre.emprunter())
        self.assertTrue(self.livre.est_emprunte)
        # Un second emprunt doit échouer.
        self.assertFalse(self.livre.emprunter())

    def test_retourner(self):
        # Si le livre n'est pas emprunté, le retour échoue.
        self.assertFalse(self.livre.retourner())
        # Après emprunt, le retour doit réussir.
        self.livre.emprunter()
        self.assertTrue(self.livre.retourner())
        self.assertFalse(self.livre.est_emprunte)
        # Un second retour doit échouer.
        self.assertFalse(self.livre.retourner())

class TestBibliotheque(unittest.TestCase):
    def setUp(self):
        self.bibliotheque = Bibliotheque()
        self.livre1 = Livre("Harry Potter", "J.K. Rowling")
        self.livre2 = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien")
        self.bibliotheque.ajouter_livre(self.livre1)
        self.bibliotheque.ajouter_livre(self.livre2)

    def test_emprunter_livre(self):
        # Emprunter "Harry Potter" doit réussir la première fois et échouer ensuite.
        self.assertTrue(self.bibliotheque.emprunter_livre("Harry Potter"))
        self.assertFalse(self.bibliotheque.emprunter_livre("Harry Potter"))
        # Même chose pour "Le Seigneur des Anneaux".
        self.assertTrue(self.bibliotheque.emprunter_livre("Le Seigneur des Anneaux"))
        self.assertFalse(self.bibliotheque.emprunter_livre("Le Seigneur des Anneaux"))

    def test_retourner_livre(self):
        # Emprunter les livres pour ensuite les retourner.
        self.bibliotheque.emprunter_livre("Harry Potter")
        self.bibliotheque.emprunter_livre("Le Seigneur des Anneaux")
        self.assertTrue(self.bibliotheque.retourner_livre("Harry Potter"))
        self.assertFalse(self.bibliotheque.retourner_livre("Harry Potter"))
        self.assertTrue(self.bibliotheque.retourner_livre("Le Seigneur des Anneaux"))
        self.assertFalse(self.bibliotheque.retourner_livre("Le Seigneur des Anneaux"))

    def test_livre_inexistant(self):
        # Tenter d'emprunter ou retourner un livre inexistant doit renvoyer False.
        self.assertFalse(self.bibliotheque.emprunter_livre("inexistant"))
        self.assertFalse(self.bibliotheque.retourner_livre("inexistant"))
    
if __name__ == '__main__':
    unittest.main()