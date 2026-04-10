import unittest
from app import Livre, Bibliotheque


# ──────────────────────────────────────────────
#  Tests unitaires pour la classe Livre
# ──────────────────────────────────────────────
class TestLivre(unittest.TestCase):

    def setUp(self):
        """Créer un livre avant chaque test."""
        self.livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")

    # --- __init__ ---
    def test_creation_titre(self):
        """Le titre doit être correctement initialisé."""
        self.assertEqual(self.livre.titre, "Le Petit Prince")

    def test_creation_auteur(self):
        """L'auteur doit être correctement initialisé."""
        self.assertEqual(self.livre.auteur, "Antoine de Saint-Exupéry")

    def test_creation_non_emprunte(self):
        """Un nouveau livre ne doit pas être emprunté."""
        self.assertFalse(self.livre.est_emprunte)

    def test_emprunter_livre_disponible(self):
        """Emprunter un livre disponible doit retourner True."""
        resultat = self.livre.emprunter()
        self.assertTrue(resultat)

    def test_emprunter_change_statut(self):
        """Après emprunt, est_emprunte doit être True."""
        self.livre.emprunter()
        self.assertTrue(self.livre.est_emprunte)

    def test_emprunter_livre_deja_emprunte(self):
        """Emprunter un livre déjà emprunté doit retourner False."""
        self.livre.emprunter()
        resultat = self.livre.emprunter()
        self.assertFalse(resultat)


    def test_retourner_livre_emprunte(self):
        """Retourner un livre emprunté doit retourner True."""
        self.livre.emprunter()
        resultat = self.livre.retourner()
        self.assertTrue(resultat)

    def test_retourner_change_statut(self):
        """Après retour, est_emprunte doit être False."""
        self.livre.emprunter()
        self.livre.retourner()
        self.assertFalse(self.livre.est_emprunte)

    def test_retourner_livre_non_emprunte(self):
        """Retourner un livre non emprunté doit retourner False."""
        resultat = self.livre.retourner()
        self.assertFalse(resultat)


# ──────────────────────────────────────────────
#  Tests unitaires pour la classe Bibliotheque
# ──────────────────────────────────────────────
class TestBibliotheque(unittest.TestCase):

    def setUp(self):
        """Créer une bibliothèque avec deux livres avant chaque test."""
        self.biblio = Bibliotheque()
        self.livre1 = Livre("1984", "George Orwell")
        self.livre2 = Livre("Dune", "Frank Herbert")
        self.biblio.ajouter_livre(self.livre1)
        self.biblio.ajouter_livre(self.livre2)

    # --- ajouter_livre() ---
    def test_ajouter_livre(self):
        """Ajouter un livre doit augmenter la taille de la liste."""
        nouveau = Livre("Fondation", "Isaac Asimov")
        self.biblio.ajouter_livre(nouveau)
        self.assertEqual(len(self.biblio.livres), 3)

    def test_ajouter_livre_present_dans_liste(self):
        """Le livre ajouté doit se trouver dans la liste."""
        nouveau = Livre("Fondation", "Isaac Asimov")
        self.biblio.ajouter_livre(nouveau)
        self.assertIn(nouveau, self.biblio.livres)

    # --- emprunter_livre() ---
    def test_emprunter_livre_existant(self):
        """Emprunter un livre existant et disponible doit retourner True."""
        resultat = self.biblio.emprunter_livre("1984")
        self.assertTrue(resultat)

    def test_emprunter_livre_change_statut(self):
        """Après emprunt via la bibliothèque, le livre doit être marqué emprunté."""
        self.biblio.emprunter_livre("1984")
        self.assertTrue(self.livre1.est_emprunte)

    def test_emprunter_livre_deja_emprunte(self):
        """Emprunter un livre déjà emprunté doit retourner False."""
        self.biblio.emprunter_livre("1984")
        resultat = self.biblio.emprunter_livre("1984")
        self.assertFalse(resultat)

    def test_emprunter_livre_inexistant(self):
        """Emprunter un livre qui n'existe pas doit retourner False."""
        resultat = self.biblio.emprunter_livre("Titre Inconnu")
        self.assertFalse(resultat)

    # --- retourner_livre() ---
    def test_retourner_livre_emprunte(self):
        """Retourner un livre emprunté doit retourner True."""
        self.biblio.emprunter_livre("Dune")
        resultat = self.biblio.retourner_livre("Dune")
        self.assertTrue(resultat)

    def test_retourner_livre_change_statut(self):
        """Après retour via la bibliothèque, le livre doit être disponible."""
        self.biblio.emprunter_livre("Dune")
        self.biblio.retourner_livre("Dune")
        self.assertFalse(self.livre2.est_emprunte)

    def test_retourner_livre_non_emprunte(self):
        """Retourner un livre non emprunté doit retourner False."""
        resultat = self.biblio.retourner_livre("1984")
        self.assertFalse(resultat)

    def test_retourner_livre_inexistant(self):
        """Retourner un livre qui n'existe pas doit retourner False."""
        resultat = self.biblio.retourner_livre("Titre Inconnu")
        self.assertFalse(resultat)

    # --- bibliothèque vide ---
    def test_emprunter_bibliotheque_vide(self):
        """Emprunter dans une bibliothèque vide doit retourner False."""
        biblio_vide = Bibliotheque()
        self.assertFalse(biblio_vide.emprunter_livre("1984"))

    def test_retourner_bibliotheque_vide(self):
        """Retourner dans une bibliothèque vide doit retourner False."""
        biblio_vide = Bibliotheque()
        self.assertFalse(biblio_vide.retourner_livre("1984"))


if __name__ == "__main__":
    unittest.main()
