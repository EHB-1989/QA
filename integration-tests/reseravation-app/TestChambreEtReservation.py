import unittest

from chambre import Chambre
from reservation import Reservation

class TestChambreEtReservation(unittest.TestCase):
    def setUp(self):
        self.chambre1 = Chambre("Chambre simple", 1, 100)
        self.chambre2 = Chambre("Chambre double", 2, 250)
        self.reservation = Reservation(self.chambre1, 2, 0)

    def test_calculer_cout(self):
        self.assertEqual(self.reservation.calculer_cout(), 200)