import unittest
from chambre import Chambre
from reservation import Reservation


class TestIntegrationRerservation(unittest.TestCase):
    def test_reservation_sans_promotion(self):
        chambre = Chambre(0,100)
        reservation = Reservation(chambre,1)
        self.assertEqual(reservation.calculer_cout(), 100)

    def test_reservation_avec_promotion(self):
            chambre = Chambre(0,100)
            reservation = Reservation(chambre,1,10)
            self.assertEqual(reservation.calculer_cout(), 90)

    def test_reservation_annulation(self):
        chambre = Chambre(0,100)
        reservation = Reservation(chambre,1)
        self.assertEqual(reservation.annuler(50), 50)

    def test_reservation_annulation_avec_frais(self):
        chambre = Chambre(0,100)
        reservation = Reservation(chambre,1)
        self.assertEqual(reservation.annuler(50), 50)

    def test_reservation_annulation_sans_frais(self):
        chambre = Chambre(0,100)
        reservation = Reservation(chambre,1)
        self.assertEqual(reservation.annuler(0), 0)


if __name__ =="__main__":
    unittest.main()