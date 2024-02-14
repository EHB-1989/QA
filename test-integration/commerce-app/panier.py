from produit import *

class Panier:
    total = 0
    produits = []
    def __init__(self, produits):
            self.produits = produits

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