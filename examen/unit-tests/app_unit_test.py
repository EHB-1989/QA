import unittest
from app import Livre, Bibliotheque

class LivreTest(unittest.TestCase):
    def setUp(self):
        self.livre = Livre("abc","def")

    # Petite application basique, donc je teste tout le cycle de vie d'un coup plutôt que séparer emprunt et retour
    def test_emprunt(self):
        # On vérifie qu'un emprunt retourne True et que son statut est "emprunté"
        self.assertTrue(self.livre.emprunter())
        self.assertTrue(self.livre.est_emprunte)

        # On vérifie que si on re-emprunte on retourne False et que le statut ne change pas
        self.assertFalse(self.livre.emprunter())
        self.assertTrue(self.livre.est_emprunte)

        # On teste le retour
        self.assertTrue(self.livre.retourner())
        self.assertFalse(self.livre.est_emprunte)

        # On vérifie qu'en répétant, on garde le bon etat & statut
        self.assertFalse(self.livre.retourner())
        self.assertFalse(self.livre.est_emprunte)


class BibliothequeTest(unittest.TestCase):
    def setUp(self):
        self.bibliotheque = Bibliotheque()
        self.livre = Livre("abc","def")

    # On vérifie que la composition entre livre et bibliothèque ne cause pas de probleme
    def test_ajout(self):
        self.assertEqual(len(self.bibliotheque.livres),0) # Pour être sur de l'état initial
        self.bibliotheque.ajouter_livre(self.livre)
        self.assertEqual(len(self.bibliotheque.livres),1)
        self.bibliotheque.livres = [] # Toujours pour être sur de pas causer de problème sur le reste des tests (on controle l'état)

    def test_emprunt(self):
        self.bibliotheque.ajouter_livre(self.livre)

        # D'abord les emprunts
        self.assertTrue(self.bibliotheque.emprunter_livre(self.livre.titre))
        # self.assertTrue(self.livre.est_emprunte) # <-- Inutile, deja testé dans la classe des livres

        self.assertFalse(self.bibliotheque.emprunter_livre(self.livre.titre))
        self.assertFalse(self.bibliotheque.emprunter_livre("Jenexistepas"))

        # Maintenant les retours
        self.assertTrue(self.bibliotheque.retourner_livre(self.livre.titre))

        self.assertFalse(self.bibliotheque.retourner_livre(self.livre.titre))
        self.assertFalse(self.bibliotheque.retourner_livre("Jenexistepas"))


if __name__ == '__main__':
    unittest.main()

