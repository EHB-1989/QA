class Reservation:
    def __init__(self, chambre, nb_nuits, promotion=0):
        self.chambre = chambre
        self.nb_nuits = nb_nuits
        self.promotion = promotion
        self.est_annulee = False

    def calculer_cout(self):
        if self.est_annulee:
            return 0
        cout_total = self.chambre.prix_saison * self.nb_nuits
        return cout_total - cout_total * self.promotion / 100

    def annuler(self, frais_annulation):
        """Annule la réservation avec des frais d'annulation."""
        self.est_annulee = True
        if frais_annulation > 0:
            return max(self.calculer_cout(), frais_annulation)
        return 0
