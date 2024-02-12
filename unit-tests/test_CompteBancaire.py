# scénario de test unitaire pour CompteBancaire
    # quand on fait un depot la fonction depot retour true
    # le solde doit etre supperieur au montant ajouter
    # le test_


from CompteBancaire import CompteBancaire


def test_initial():
    compte = CompteBancaire(100)
    assert compte.get_solde() == 100

def test_depot():
    compte = CompteBancaire()
    assert compte.depot(20) is True
    assert compte.depot(-20) is False
    assert compte.get_solde() == 20

def test_retrait():
    compte = CompteBancaire(100)
    assert compte.retrait(50) is True
    assert compte.retrait(200) is False
    assert compte.retrait(-20) is False
    assert compte.get_solde() == 50



def run_test():
    test_depot()
    test_retrait()

run_test()