class Inventaire:
    def __init__(self):
        self.produits = {}
 
    def ajouter_produit(self, nom, quantite):
        if quantite <= 0:
            return False
        if nom in self.produits:
            self.produits[nom] += quantite
        else:
            self.produits[nom] = quantite
        return True

    def supprimer_produit(self, nom, quantite):
        if nom not in self.produits or quantite <= 0 or self.produits[nom] < quantite:
            return False
        self.produits[nom] -= quantite
        if self.produits[nom] == 0:
            del self.produits[nom]
        return True

    def rechercher_produit(self, nom):
        return self.produits.get(nom, 0)
