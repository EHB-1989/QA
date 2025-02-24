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

def test_livre():
    livre = Livre("Harry Potter", "J.K. Rowling")
    assert livre.titre == "Harry Potter"
    assert livre.auteur == "J.K. Rowling"
    assert not livre.est_emprunte # Le livre ne doit pas être emprunté puisque l'on vient de le créer
    assert livre.emprunter() # On vérifie si l'emprunt du livre retourne True
    assert livre.est_emprunte # on vérifie que le livre est bien considéré comme emprunté
    assert not livre.emprunter() # Le livre est déjà emprunté, on ne peut donc pas l'emprunter une deuxième fois
    assert livre.retourner() # On vérifie si le retour du livre retourne True
    assert not livre.est_emprunte # on vérifie que le livre est bien considéré comme non emprunté
    assert not livre.retourner() # Le livre n'est pas emprunté, on ne peut donc pas le retourner
    
def test_bibliotheque():
    bibliotheque = Bibliotheque()
    livre1 = Livre("Harry Potter", "J.K. Rowling")
    livre2 = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien")
    bibliotheque.ajouter_livre(livre1)
    bibliotheque.ajouter_livre(livre2)
    assert bibliotheque.emprunter_livre("Harry Potter") # On vérifie si l'emprunt du livre retourne True
    assert not bibliotheque.emprunter_livre("Harry Potter") # Le livre est déjà emprunté, on ne peut donc pas l'emprunter une deuxième fois
    assert bibliotheque.emprunter_livre("Le Seigneur des Anneaux") # On vérifie si l'emprunt du livre retourne True
    assert not bibliotheque.emprunter_livre("Le Seigneur des Anneaux") # Le livre est déjà emprunté, on ne peut donc pas l'emprunter une deuxième fois
    assert bibliotheque.retourner_livre("Harry Potter") # On vérifie si le retour du livre retourne True
    assert not bibliotheque.retourner_livre("Harry Potter") # Le livre n'est pas emprunté, on ne peut donc pas le retourner
    assert bibliotheque.retourner_livre("Le Seigneur des Anneaux") # On vérifie si le retour du livre retourne True
    assert not bibliotheque.retourner_livre("Le Seigneur des Anneaux") # Le livre n'est pas emprunté, on ne peut donc pas le retourner
    
    assert not bibliotheque.emprunter_livre("inexistant") # le livre n'existe pas, on ne peut donc pas l'emprunter
    assert not bibliotheque.retourner_livre("inexistant") # le livre n'existe pas, on ne peut donc pas le retourner
    
    
if __name__ == '__main__':
    test_livre()
    test_bibliotheque()
    print("Tous les tests passent")