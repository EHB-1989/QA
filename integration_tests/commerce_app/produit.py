# class Produit:
#     def __init__(self, nom, prix):
#         self.nom = nom
#         self.prix = prix


class Produit:
    def __init__(self, nom, prix, quantite_en_stock, pourcentage_remise=0):
        self.nom = nom
        self.prix = prix
        self.quantite_en_stock = quantite_en_stock
        self.pourcentage_remise = pourcentage_remise

    def acheter(self, quantite):
        """Diminue la quantité en stock du produit."""
        if quantite <= self.quantite_en_stock:
            self.quantite_en_stock -= quantite
            return True
        else:
            return False

    def calculer_prix_apres_remise(self):
        """Calcule le prix du produit après l'application de la remise."""
        prix_apres_remise = self.prix * (1 - self.pourcentage_remise / 100)
        return round(prix_apres_remise, 2)

