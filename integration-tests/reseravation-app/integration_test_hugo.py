import unittest
from chambre import Chambre 
from reservation import Reservation

class TestReservationIntegration(unittest.TestCase):
    
    def test_reservation_cout_sans_promotion(self):
        chambre = Chambre(101, 100)
        reservation = Reservation(chambre, 3)
        self.assertEqual(reservation.calculer_cout(), 300)
    
    def test_reservation_cout_avec_promotion(self):
        chambre = Chambre(102, 200)
        reservation = Reservation(chambre, 2, promotion=10)
        self.assertEqual(reservation.calculer_cout(), 360)
    
    def test_reservation_cout_avec_saison(self):
        chambre = Chambre(103, 150)
        chambre.definir_prix_saison(1.5)  # Prix saison = 150 * 1.5 = 225
        reservation = Reservation(chambre, 4)
        self.assertEqual(reservation.calculer_cout(), 900)
    
    def test_annulation_sans_frais(self):
        chambre = Chambre(104, 120)
        reservation = Reservation(chambre, 2)
        reservation.annuler(frais_annulation=0)
        self.assertEqual(reservation.calculer_cout(), 0)
    
    def test_annulation_avec_frais(self):
        chambre = Chambre(105, 100)
        reservation = Reservation(chambre, 3)
        frais = reservation.annuler(frais_annulation=50)
        self.assertEqual(frais, 50)
    
    def test_annulation_avec_frais_superieur_au_cout(self):
        chambre = Chambre(106, 80)
        reservation = Reservation(chambre, 1)
        frais = reservation.annuler(frais_annulation=200)
        self.assertEqual(frais, 200)

if __name__ == '__main__':
    unittest.main()
