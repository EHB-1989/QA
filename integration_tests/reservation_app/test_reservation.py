from integration_tests.reservation_app.chambre import Chambre
from integration_tests.reservation_app.reservation import Reservation
from pytest import fixture


@fixture
def chambre_de_base():
    return Chambre(1, 100)

@fixture
def chambre_avec_multiplicateur():
    chambre = Chambre(2, 100)
    chambre.definir_prix_saison(2)
    return chambre

@fixture
def reservation_avec_deux_nuits(chambre_avec_multiplicateur):
    """ Price returned should be 400 with saison, else 200"""
    return Reservation(chambre_avec_multiplicateur, 2)

### ---- TESTS ----  ###

def test_reservation_avec_prix_de_base(chambre_de_base):
    reservation = Reservation(chambre_de_base, 2)
    assert reservation.calculer_cout() == 200

def test_reservation_avec_prix_saison(reservation_avec_deux_nuits):
    assert reservation_avec_deux_nuits.calculer_cout() == 400

def test_annuler_reservation_should_match_cost(reservation_avec_deux_nuits):
    assert reservation_avec_deux_nuits.annuler(500) == 500
    assert reservation_avec_deux_nuits.est_annulee == True

def test_annuler_reservation_should_be_higher_than_cost(reservation_avec_deux_nuits):
    assert reservation_avec_deux_nuits.annuler(1000) == 1000
    assert reservation_avec_deux_nuits.est_annulee == True

def test_reservation_should_have_promotion(reservation_avec_deux_nuits):
    reservation_avec_deux_nuits.promotion = 30
    assert reservation_avec_deux_nuits.calculer_cout() == 280

