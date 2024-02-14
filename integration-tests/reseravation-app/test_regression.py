from chambre import Chambre
from reservation import Reservation

def test_calcul_cout_reservation():
    chambre = Chambre(101, 100)
    chambre.definir_prix_saison(1.2)
    reservation = Reservation(chambre, 2)

    cout_total = reservation.calculer_cout()
    assert cout_total == 240

    reservation.promotion = 10
    cout_total = reservation.calculer_cout()
    assert cout_total == 216

    reservation.annuler(50)
    assert reservation.est_annulee is True
    assert reservation.calculer_cout() == 50
