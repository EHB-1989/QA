from produit import *

class Panier:
    total = 0
    produits = []

    def getProduits(self):
        return self.produits
    def getTotal(self):
        return self.total

    def add(self, produit, nb):
        if nb > 0:
            self.total += produit.getPrix() * nb
            produit.setStock(produit.getStock() - nb)
            self.produits.append(produit)

    def remove(self, produit, nb):
        if nb > 0:
            self.total -= produit.getPrix() * nb
            produit.setStock(produit.getStock() + nb)
            for i in range(nb):
                self.produits.remove(produit)