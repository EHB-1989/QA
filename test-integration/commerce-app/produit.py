class Produit:
        def __init__(self, nb, prix, remise):
            self.stock = nb
            self.prix = prix
            self.remise = remise

        def getPrix(self):
              return self.prix
        def getStock(self):
              return self.stock
        def getRemise(self):
              return self.remise
        def setStock(self,nb):
              self.stock = nb