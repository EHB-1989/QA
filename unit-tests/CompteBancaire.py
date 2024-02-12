class CompteBancaire:
    def __init__(self, solde_initial=0):
        self.solde = solde_initial

    def depot(self, montant):
        if montant > 0:
            self.solde += montant
            return True
        return False

    def retrait(self, montant):
        if montant > 0 and self.solde - montant >= 0:
            self.solde -= montant
            return True
        return False

    def get_solde(self):
        return self.solde
