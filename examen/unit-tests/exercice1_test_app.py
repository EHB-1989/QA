import unittest
from app import Livre, Bibliotheque


# =========================
# Tests pour la classe Livre
# =========================
class TestLivre(unittest.TestCase):

    # Méthode exécutée avant chaque test
    def setUp(self):
        # On crée un livre de base pour tous les tests
        self.livre = Livre("Le tour du monde en 80 jours", "Jules Verne")

    # Test de la création d’un livre
    def test_creation_livre(self):
        self.assertEqual(self.livre.titre, "Le tour du monde en 80 jours") # Vérifie le titre
        self.assertEqual(self.livre.auteur, "Jules Verne") # Vérifie l’auteur
        self.assertFalse(self.livre.est_emprunte) # Doit être disponible au départ

    # Test emprunt d’un livre disponible
    def test_emprunter_livre_disponible(self):
        resultat = self.livre.emprunter()
        self.assertTrue(resultat) # L’emprunt doit réussir
        self.assertTrue(self.livre.est_emprunte) # Le livre devient emprunté

    # Test emprunt d’un livre déjà emprunté
    def test_emprunter_livre_deja_emprunte(self):
        self.livre.emprunter() # On l’emprunte une première fois
        resultat = self.livre.emprunter() # On essaie de nouveau
        self.assertFalse(resultat) # Doit échouer

    # Test retour d’un livre emprunté
    def test_retourner_livre_emprunte(self):
        self.livre.emprunter() # On l’emprunte d’abord
        resultat = self.livre.retourner()
        self.assertTrue(resultat) # Le retour doit réussir
        self.assertFalse(self.livre.est_emprunte) # Le livre redevient disponible

    # Test retour d’un livre qui n’est pas emprunté
    def test_retourner_livre_non_emprunte(self):
        resultat = self.livre.retourner()
        self.assertFalse(resultat) # Doit échouer


# =========================
# Tests pour la classe Bibliotheque
# =========================
class TestBibliotheque(unittest.TestCase):

    # Initialisation avant chaque test
    def setUp(self):
        self.biblio = Bibliotheque()

        # Création de deux livres
        self.livre1 = Livre("Le tour du monde en 80 jours", "Jules Verne")
        self.livre2 = Livre("Dune", "Frank Herbert")

        # Ajout des livres à la bibliothèque
        self.biblio.ajouter_livre(self.livre1)
        self.biblio.ajouter_livre(self.livre2)

    # Test ajout d’un livre
    def test_ajouter_livre(self):
        livre3 = Livre("Le seigneur des anneaux", "J.R.R. Tolkien")
        self.biblio.ajouter_livre(livre3)
        self.assertIn(livre3, self.biblio.livres) # Vérifie qu’il est bien ajouté

    # Test emprunt d’un livre existant
    def test_emprunter_livre_existant(self):
        resultat = self.biblio.emprunter_livre("Le tour du monde en 80 jours")
        self.assertTrue(resultat) # Doit réussir
        self.assertTrue(self.livre1.est_emprunte) # Le livre est marqué emprunté

    # Test emprunt d’un livre inexistant
    def test_emprunter_livre_inexistant(self):
        resultat = self.biblio.emprunter_livre("Livre inconnu")
        self.assertFalse(resultat) # Doit échouer

    # Test emprunt d’un livre déjà emprunté
    def test_emprunter_livre_deja_emprunte(self):
        self.biblio.emprunter_livre("Le tour du monde en 80 jours") # Premier emprunt
        resultat = self.biblio.emprunter_livre("Le tour du monde en 80 jours") # Deuxième tentative
        self.assertFalse(resultat) # Doit échouer

    # Test retour d’un livre emprunté
    def test_retourner_livre_emprunte(self):
        self.biblio.emprunter_livre("Le tour du monde en 80 jours") # On emprunte
        resultat = self.biblio.retourner_livre("Le tour du monde en 80 jours")
        self.assertTrue(resultat) # Le retour doit réussir
        self.assertFalse(self.livre1.est_emprunte) # Le livre redevient disponible

    # Test retour d’un livre non emprunté
    def test_retourner_livre_non_emprunte(self):
        resultat = self.biblio.retourner_livre("Le tour du monde en 80 jours")
        self.assertFalse(resultat) # Doit échouer

    # Test retour d’un livre inexistant
    def test_retourner_livre_inexistant(self):
        resultat = self.biblio.retourner_livre("Livre inconnu")
        self.assertFalse(resultat) # Doit échouer


# Permet d’exécuter les tests directement
if __name__ == "__main__":
    unittest.main()