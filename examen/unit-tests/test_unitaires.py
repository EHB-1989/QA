class TestBibliotheque(unittest.TestCase):

    def setUp(self):
        """Avant chaque test, on crée une bibliothèque et quelques livres"""
        self.bibliotheque = Bibliotheque()
        self.livre1 = Livre("1984", "George Orwell")
        self.livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")
        self.livre3 = Livre("Les Misérables", "Victor Hugo")
        self.bibliotheque.ajouter_livre(self.livre1)
        self.bibliotheque.ajouter_livre(self.livre2)
        self.bibliotheque.ajouter_livre(self.livre3)

    def test_emprunter_livre_disponible(self):
        """Tester qu'on peut emprunter un livre disponible"""
        result = self.bibliotheque.emprunter_livre("1984")
        self.assertTrue(result)
        self.assertTrue(self.livre1.est_emprunte)

    def test_emprunter_livre_indisponible(self):
        """Tester qu'on ne peut pas emprunter un livre déjà emprunté"""
        self.bibliotheque.emprunter_livre("1984")
        result = self.bibliotheque.emprunter_livre("1984")
        self.assertFalse(result)

    def test_retourner_livre(self):
        """Tester qu'on peut retourner un livre emprunté"""
        self.bibliotheque.emprunter_livre("1984")
        result = self.bibliotheque.retourner_livre("1984")
        self.assertTrue(result)
        self.assertFalse(self.livre1.est_emprunte)

    def test_retourner_livre_non_emprunte(self):
        """Tester qu'on ne peut pas retourner un livre non emprunté"""
        result = self.bibliotheque.retourner_livre("1984")
        self.assertFalse(result)

    def test_emprunter_livre_non_existant(self):
        """Tester qu'on ne peut pas emprunter un livre qui n'existe pas"""
        result = self.bibliotheque.emprunter_livre("Le Hobbit")
        self.assertFalse(result)

    def test_retourner_livre_non_existant(self):
        """Tester qu'on ne peut pas retourner un livre qui n'existe pas"""
        result = self.bibliotheque.retourner_livre("Le Hobbit")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()