from chambre import Chambre
from reservation import Reservation
import unittest

class TestReservation(unittest.TestCase):
    def test_calculer_cout(self):
        chambre = Chambre(100, 50)
        reservation = Reservation(chambre, 3)
        self.assertEqual(reservation.calculer_cout(), 150)
        reservation = Reservation(chambre, 2, 10)
        self.assertEqual(reservation.calculer_cout(), 90)

    def test_annuler(self):
        chambre = Chambre(100, 50)
        reservation = Reservation(chambre, 3)
        self.assertEqual(reservation.annuler(0), 0)
        self.assertEqual(reservation.annuler(20), 20)

if __name__ == '__main__':
    unittest.main()