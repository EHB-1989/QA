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
