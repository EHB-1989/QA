import Chambre, Reservation
import unittest

class TestReservation(unittest.TestCase):
    
    def setUp(self):
        self.chambre = Chambre.Chambre(numero=101, prix_base=100)
        self.reservation = Reservation.Reservation(chambre=self.chambre, nb_nuits=3)

    def test_calculer_cout_sans_promotion(self):
        self.chambre.definir_prix_saison(multiplicateur_saison=1.0)
        cout = self.reservation.calculer_cout()
        self.assertEqual(cout, 300)

    def test_calculer_cout_avec_promotion(self):
        self.chambre.definir_prix_saison(multiplicateur_saison=1.0)
        self.reservation.promotion = 20
        cout = self.reservation.calculer_cout()
        self.assertEqual(cout, 220, "le cout est incorrect")



if __name__ == '__main__':
    unittest.main()
