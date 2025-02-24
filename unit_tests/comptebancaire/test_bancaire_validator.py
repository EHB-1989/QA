#test_bancaire_validator.py
from unit_tests.comptebancaire.CompteBancaire import CompteBancaire

def test_bancaire_initialisation():
    compte = CompteBancaire()
    assert compte.get_solde() == 0, "Le solde initial devrait être 0."
    compte = CompteBancaire(2000)
    assert compte.get_solde() == 2000, "On vérifie le solde à 2000"


def test_bancaire_depot_echec():
    compte = CompteBancaire(50)
    assert compte.depot(-20) is False, "Le dépôt avec un montant négatif ne devrait pas être autorisé...."
    assert compte.get_solde() == 50, "Normalement le solde ne devrait pas changer après un dépôt invalide."


def test_bancaire_depot_succes():
    compte = CompteBancaire(50)
    assert compte.depot(10) is True, "Le dépôt devrait réussir !"
    assert compte.get_solde() == 60, "Le solde après un dépôt de 10 devrait être 60."

def test_bancaire_retrait_succes():
    compte = CompteBancaire(1200)
    assert compte.retrait(30) is True, "Le retrait devrait réussir ! "
    assert compte.get_solde() == 1170, "Le solde après un retrait de 30 devrait être 1170."


def test_bancaire_retrait_echec_fonds_insuffisants():
    compte = CompteBancaire(50)
    assert compte.retrait(60) is False, "Le retrait ne devrait pas être autorisé si les fonds sont insuffisants ! "
    assert compte.get_solde() == 50, "Idem, le solde ne devrait pas changer après un retrait invalide."


def test_bancaire_retrait_echec_montant_negatif():
    compte = CompteBancaire(50)
    assert compte.retrait(-10) is False, "Le retrait avec un montant négatif ne devrait pas être autorisé..."
    assert compte.get_solde() == 50, "Encore une fois, le solde ne devrait pas changer après un retrait invalide."


def test_bancaire_comportement_combinaison_operations():
    compte = CompteBancaire(100)
    assert compte.depot(50) is True, "Le dépôt de 50 devrait réussir."
    assert compte.retrait(30) is True, "Le retrait de 30 devrait réussir."
    assert compte.retrait(200) is False, "Le retrait de 200 devrait échouer (fonds insuffisants)."
    assert compte.get_solde() == 120, "Si on n'a pas d'erreurs, le solde final devrait être 120 après ces opérations."
