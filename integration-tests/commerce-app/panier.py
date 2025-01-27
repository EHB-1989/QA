# class Panier:
#     def __init__(self):
#         self.produits = []

#     def ajouter_produit(self, produit):
#         self.produits.append(produit)

#     def calculer_total(self):
#         return sum(produit.prix for produit in self.produits)


class Panier:
    def __init__(self):
        # Utilise un dictionnaire pour stocker les produits et leurs quantités
        self.produits = {}

    def ajouter_produit(self, produit, quantite):
        # Vérifie si le produit peut être acheté en quantité souhaitée
        if produit.acheter(quantite):
            if produit in self.produits:
                self.produits[produit] += quantite
            else:
                self.produits[produit] = quantite
        else:
            print(
                f"Impossible d'ajouter {quantite} de {produit.nom} en raison du stock insuffisant."
            )

    def calculer_total(self):
        total = 0
        for produit, quantite in self.produits.items():
            total += produit.calculer_prix_apres_remise() * quantite
        return total
