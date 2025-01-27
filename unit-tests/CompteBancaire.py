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


if __name__ == "__main__":
    print("Début des tets")

    compte = CompteBancaire()
    print(compte.get_solde)
    assert compte.get_solde() == 0, "Echec le solde initial n'est pas zéro"
    compte.depot(10)
    assert compte.get_solde() == 10, "Le solde doit être de 10"
    compte.retrait(10)
    assert compte.get_solde() == 0, "Le solde doit être de 0"
