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

def test_CompteBancaire():
    compte=CompteBancaire(100)
    assert compte.get_solde() == 100
    assert compte.retrait(-50) == False
    assert compte.retrait(150) == False
    assert compte.retrait(100) == True
    assert compte.get_solde() == 0
    assert compte.depot(-50) == False
    assert compte.depot(50) == True

test_CompteBancaire()
    