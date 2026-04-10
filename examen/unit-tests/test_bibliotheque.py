"""Tests unitaires (unittest) : comportement de Livre et Bibliotheque."""
import unittest

from app import Bibliotheque, Livre

class TestLivre(unittest.TestCase):
    def test_init_attribue_titre_auteur_et_non_emprunte(self):
        livre = Livre("1984", "Orwell")
        self.assertEqual(livre.titre, "1984")
        self.assertEqual(livre.auteur, "Orwell")
        self.assertFalse(livre.est_emprunte)

    def test_emprunter_reussit_si_disponible(self):
        livre = Livre("Dune", "Herbert")
        self.assertTrue(livre.emprunter())
        self.assertTrue(livre.est_emprunte)

    def test_emprunter_echoue_si_deja_emprunte(self):
        livre = Livre("Dune", "Herbert")
        livre.emprunter()
        # Double emprunt : doit rester refusé sans changer l'état de façon incohérente.
        self.assertFalse(livre.emprunter())
        self.assertTrue(livre.est_emprunte)

    def test_retourner_reussit_si_emprunte(self):
        livre = Livre("Dune", "Herbert")
        livre.emprunter()
        self.assertTrue(livre.retourner())
        self.assertFalse(livre.est_emprunte)

    def test_retourner_echoue_si_pas_emprunte(self):
        livre = Livre("Dune", "Herbert")
        # Retour sans emprunt préalable : pas de changement d'état.
        self.assertFalse(livre.retourner())
        self.assertFalse(livre.est_emprunte)


class TestBibliotheque(unittest.TestCase):
    """Inventaire : recherche par titre et cohérence avec Livre.emprunter / retourner."""

    def test_init_inventaire_vide(self):
        bib = Bibliotheque()
        self.assertEqual(bib.livres, [])

    def test_ajouter_livre_ajoute_a_l_inventaire(self):
        bib = Bibliotheque()
        l = Livre("Le Petit Prince", "Saint-Exupéry")
        bib.ajouter_livre(l)
        self.assertEqual(len(bib.livres), 1)
        # Même instance que celle ajoutée (pas de copie implicite).
        self.assertIs(bib.livres[0], l)

    def test_emprunter_livre_reussit_si_titre_present_et_disponible(self):
        bib = Bibliotheque()
        bib.ajouter_livre(Livre("Hamlet", "Shakespeare"))
        self.assertTrue(bib.emprunter_livre("Hamlet"))
        self.assertTrue(bib.livres[0].est_emprunte)

    def test_emprunter_livre_echoue_si_titre_inconnu(self):
        bib = Bibliotheque()
        bib.ajouter_livre(Livre("Hamlet", "Shakespeare"))
        self.assertFalse(bib.emprunter_livre("Macbeth"))

    def test_emprunter_livre_echoue_si_deja_emprunte(self):
        bib = Bibliotheque()
        bib.ajouter_livre(Livre("Hamlet", "Shakespeare"))
        self.assertTrue(bib.emprunter_livre("Hamlet"))
        self.assertFalse(bib.emprunter_livre("Hamlet"))

    def test_retourner_livre_reussit_si_emprunte(self):
        bib = Bibliotheque()
        bib.ajouter_livre(Livre("Hamlet", "Shakespeare"))
        bib.emprunter_livre("Hamlet")
        self.assertTrue(bib.retourner_livre("Hamlet"))
        self.assertFalse(bib.livres[0].est_emprunte)

    def test_retourner_livre_echoue_si_pas_emprunte(self):
        bib = Bibliotheque()
        bib.ajouter_livre(Livre("Hamlet", "Shakespeare"))
        self.assertFalse(bib.retourner_livre("Hamlet"))

    def test_retourner_livre_echoue_si_titre_inconnu(self):
        bib = Bibliotheque()
        bib.ajouter_livre(Livre("Hamlet", "Shakespeare"))
        bib.emprunter_livre("Hamlet")
        # Mauvais titre : ne doit pas affecter l'exemplaire emprunté.
        self.assertFalse(bib.retourner_livre("Macbeth"))

    def test_plusieurs_livres_meme_titre_emprunte_le_premier_disponible(self):
        # Deux exemplaires même titre : la boucle emprunte d'abord le 1er libre, puis le 2e.
        bib = Bibliotheque()
        bib.ajouter_livre(Livre("Python", "A"))
        bib.ajouter_livre(Livre("Python", "B"))
        self.assertTrue(bib.emprunter_livre("Python"))
        self.assertTrue(bib.emprunter_livre("Python"))
        self.assertTrue(bib.livres[0].est_emprunte)
        self.assertTrue(bib.livres[1].est_emprunte)


if __name__ == "__main__":
    unittest.main()
