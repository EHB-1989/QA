class Chambre:
    def __init__(self, numero, prix_base):
        self.numero = numero
        self.prix_base = prix_base
        self.prix_saison = prix_base

    def definir_prix_saison(self, multiplicateur_saison):
        """Ajuste le prix par nuit selon un multiplicateur de saison."""
        self.prix_saison = self.prix_base * multiplicateur_saison
