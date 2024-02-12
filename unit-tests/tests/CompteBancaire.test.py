import CompteBancaire

def test_compte_bancaire_depot():
    compte_1 = CompteBancaire(5000)
    assert compte_1.depot(-500) == False
    assert compte_1.depot(0) == False
    assert compte_1.depot(20) == True
    assert compte_1.get_solde() == 5020
    
    compte_2 = CompteBancaire(-20)
    assert compte_2.depot(30) == True
    assert compte_2.get_solde() == 10

def test_compte_bancaire_retrait():
    compte_1 = CompteBancaire(5000)
    assert compte_1.retrait(-400) == False
    assert compte_1.retrait(5000) == False
    assert compte_1.retrait(100) == True
    assert compte_1.get_solde() == 4900
    
    compte_2 = CompteBancaire(-20)
    assert compte_2.retrait(-30) == False
    assert compte_2.retrait(250) == False
    assert compte_2.get_solde() == -20
    
def test_compte_bancaire_retrait():
    compte_1 = CompteBancaire(5000)
    assert compte_1.get_solde() == 5000
    
    compte_2 = CompteBancaire(-5000)
    assert compte_2.get_solde() == -5000
