class Produit:
    def __init__(self,nom, nb, prix, remise):
        self.nom = nom
        self.stock = nb
        self.prix = prix
        self.remise = remise

    def getNom(self):
        return self.nom
    def getPrix(self):
          return self.prix
    def getStock(self):
          return self.stock
    def getRemise(self):
          return self.remise
    def setStock(self,nb):
          self.stock = nb