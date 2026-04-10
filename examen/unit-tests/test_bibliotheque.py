"""
Tests unitaires - Exercice 1
Eylon Soussan & Kiara

On teste les classes Livre et Bibliotheque avec unittest.
"""

import unittest
from app import Livre, Bibliotheque


class TestLivre(unittest.TestCase):

    def setUp(self):
        # on crée un livre de base avant chaque test
        self.livre = Livre("Les Misérables", "Victor Hugo")

    def test_creation_titre(self):
        # le titre doit être correctement assigné
        self.assertEqual(self.livre.titre, "Les Misérables")

    def test_creation_auteur(self):
        # l'auteur doit être correctement assigné
        self.assertEqual(self.livre.auteur, "Victor Hugo")

    def test_livre_non_emprunte_a_la_creation(self):
        # un nouveau livre ne doit pas être emprunté par défaut
        self.assertFalse(self.livre.est_emprunte)

    def test_emprunter_livre_disponible(self):
        # emprunter un livre disponible doit retourner True
        resultat = self.livre.emprunter()
        self.assertTrue(resultat)

    def test_emprunter_change_etat(self):
        # après emprunt, est_emprunte doit passer à True
        self.livre.emprunter()
        self.assertTrue(self.livre.est_emprunte)

    def test_emprunter_livre_deja_emprunte(self):
        # on ne peut pas emprunter un livre déjà emprunté
        self.livre.emprunter()
        resultat = self.livre.emprunter()
        self.assertFalse(resultat)

    def test_double_emprunt_ne_change_pas_etat(self):
        # l'état ne doit pas changer si le 2ème emprunt échoue
        self.livre.emprunter()
        self.livre.emprunter()
        self.assertTrue(self.livre.est_emprunte)

    def test_retourner_livre_emprunte(self):
        # retourner un livre emprunté doit retourner True
        self.livre.emprunter()
        resultat = self.livre.retourner()
        self.assertTrue(resultat)

    def test_retourner_remet_livre_disponible(self):
        # après retour, le livre doit redevenir disponible
        self.livre.emprunter()
        self.livre.retourner()
        self.assertFalse(self.livre.est_emprunte)

    def test_retourner_livre_non_emprunte(self):
        # retourner un livre qui n'est pas emprunté doit retourner False
        resultat = self.livre.retourner()
        self.assertFalse(resultat)

    def test_retourner_non_emprunte_ne_change_pas_etat(self):
        # si le retour échoue, l'état ne doit pas changer
        self.livre.retourner()
        self.assertFalse(self.livre.est_emprunte)

    def test_cycle_emprunt_retour(self):
        # on doit pouvoir emprunter et retourner plusieurs fois
        self.assertTrue(self.livre.emprunter())
        self.assertTrue(self.livre.retourner())
        self.assertTrue(self.livre.emprunter())  # réemprunté après retour


class TestBibliotheque(unittest.TestCase):

    def setUp(self):
        # on initialise une bibliothèque et deux livres pour les tests
        self.bibliotheque = Bibliotheque()
        self.livre1 = Livre("1984", "George Orwell")
        self.livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")

    def test_bibliotheque_vide_au_depart(self):
        # une bibliothèque neuve ne doit contenir aucun livre
        self.assertEqual(len(self.bibliotheque.livres), 0)

    def test_ajouter_livre(self):
        # après ajout, le livre doit être dans la liste
        self.bibliotheque.ajouter_livre(self.livre1)
        self.assertIn(self.livre1, self.bibliotheque.livres)

    def test_ajouter_plusieurs_livres(self):
        # on doit pouvoir ajouter plusieurs livres
        self.bibliotheque.ajouter_livre(self.livre1)
        self.bibliotheque.ajouter_livre(self.livre2)
        self.assertEqual(len(self.bibliotheque.livres), 2)

    def test_emprunter_livre_present(self):
        # emprunter un livre présent et disponible doit réussir
        self.bibliotheque.ajouter_livre(self.livre1)
        resultat = self.bibliotheque.emprunter_livre("1984")
        self.assertTrue(resultat)

    def test_emprunter_livre_absent(self):
        # emprunter un livre qui n'existe pas doit retourner False
        resultat = self.bibliotheque.emprunter_livre("Livre Inconnu")
        self.assertFalse(resultat)

    def test_emprunter_livre_deja_emprunte(self):
        # on ne peut pas emprunter un livre déjà sorti
        self.bibliotheque.ajouter_livre(self.livre1)
        self.bibliotheque.emprunter_livre("1984")
        resultat = self.bibliotheque.emprunter_livre("1984")
        self.assertFalse(resultat)

    def test_emprunter_met_a_jour_etat_livre(self):
        # le livre doit être marqué comme emprunté dans l'objet
        self.bibliotheque.ajouter_livre(self.livre1)
        self.bibliotheque.emprunter_livre("1984")
        self.assertTrue(self.livre1.est_emprunte)

    def test_retourner_livre_emprunte(self):
        # retourner un livre emprunté doit réussir
        self.bibliotheque.ajouter_livre(self.livre1)
        self.bibliotheque.emprunter_livre("1984")
        resultat = self.bibliotheque.retourner_livre("1984")
        self.assertTrue(resultat)

    def test_retourner_livre_non_emprunte(self):
        # retourner un livre qui n'est pas sorti doit échouer
        self.bibliotheque.ajouter_livre(self.livre1)
        resultat = self.bibliotheque.retourner_livre("1984")
        self.assertFalse(resultat)

    def test_retourner_livre_absent(self):
        # retourner un livre inexistant doit retourner False
        resultat = self.bibliotheque.retourner_livre("Livre Inconnu")
        self.assertFalse(resultat)

    def test_retourner_remet_livre_disponible(self):
        # après retour, le livre doit redevenir disponible
        self.bibliotheque.ajouter_livre(self.livre1)
        self.bibliotheque.emprunter_livre("1984")
        self.bibliotheque.retourner_livre("1984")
        self.assertFalse(self.livre1.est_emprunte)

    def test_emprunt_ne_touche_pas_autres_livres(self):
        # emprunter un livre ne doit pas affecter les autres
        self.bibliotheque.ajouter_livre(self.livre1)
        self.bibliotheque.ajouter_livre(self.livre2)
        self.bibliotheque.emprunter_livre("1984")
        self.assertFalse(self.livre2.est_emprunte)


if __name__ == "__main__":
    unittest.main(verbosity=2)
