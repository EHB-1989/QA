import unittest
from app import Livre, Bibliotheque

class TestLivre(unittest.TestCase):

    def setUp(self):
        self.livre = Livre("La Nuit sacrée", "Tahar Ben Jelloun")

    def test_creation_initialisation(self):
        """Le titre, l'auteur et le statut doivent être corrects."""
        self.assertEqual(self.livre.titre, "La Nuit sacrée")
        self.assertEqual(self.livre.auteur, "Tahar Ben Jelloun")
        self.assertFalse(self.livre.est_emprunte)

    def test_emprunter_livre_disponible(self):
        """Emprunter un livre disponible doit retourner True et changer le statut."""
        self.assertTrue(self.livre.emprunter())
        self.assertTrue(self.livre.est_emprunte)

    def test_emprunter_livre_deja_emprunte(self):
        """Emprunter un livre déjà emprunté doit retourner False."""
        self.livre.emprunter()
        self.assertFalse(self.livre.emprunter())

    def test_retourner_livre_emprunte(self):
        """Retourner un livre emprunté doit retourner True et changer le statut."""
        self.livre.emprunter()
        self.assertTrue(self.livre.retourner())
        self.assertFalse(self.livre.est_emprunte)

    def test_retourner_livre_non_emprunte(self):
        """Retourner un livre non emprunté doit retourner False."""
        self.assertFalse(self.livre.retourner())


class TestBibliotheque(unittest.TestCase):

    def setUp(self):
        """Préparer une bibliothèque."""
        self.biblio = Bibliotheque()
        self.livre1 = Livre("L'Enfant de sable", "Tahar Ben Jelloun")
        self.livre2 = Livre("Le Mariage de plaisir", "Tahar Ben Jelloun")
        self.biblio.ajouter_livre(self.livre1)
        self.biblio.ajouter_livre(self.livre2)

    def test_ajouter_livre(self):
        """Ajouter un livre doit augmenter la taille et être présent dans la liste."""
        nouveau = Livre("L'Insolition", "Tahar Ben Jelloun")
        self.biblio.ajouter_livre(nouveau)
        self.assertEqual(len(self.biblio.livres), 3)
        self.assertIn(nouveau, self.biblio.livres)

    def test_emprunter_livre_bibliotheque(self):
        """Vérifie l'emprunt réussi et le changement de statut via la biblio."""
        self.assertTrue(self.biblio.emprunter_livre("L'Enfant de sable"))
        self.assertTrue(self.livre1.est_emprunte)

    def test_emprunter_livre_indisponible(self):
        """Emprunter un livre déjà pris ou inexistant doit échouer."""
        self.biblio.emprunter_livre("L'Enfant de sable")
        self.assertFalse(self.biblio.emprunter_livre("L'Enfant de sable"))
        self.assertFalse(self.biblio.emprunter_livre("Titre Inconnu"))

    def test_retourner_livre_bibliotheque(self):
        """Vérifie le retour réussi via la bibliothèque."""
        self.biblio.emprunter_livre("Le Mariage de plaisir")
        self.assertTrue(self.biblio.retourner_livre("Le Mariage de plaisir"))
        self.assertFalse(self.livre2.est_emprunte)

    def test_retourner_livre_erreur(self):
        """Retourner un livre non emprunté ou inexistant doit échouer."""
        self.assertFalse(self.biblio.retourner_livre("L'Enfant de sable"))
        self.assertFalse(self.biblio.retourner_livre("Titre Inconnu"))

    def test_bibliotheque_vide(self):
        """Vérifie le comportement avec une bibliothèque sans livres."""
        biblio_vide = Bibliotheque()
        self.assertFalse(biblio_vide.emprunter_livre("L'Enfant de sable"))


if __name__ == "__main__":
    unittest.main()