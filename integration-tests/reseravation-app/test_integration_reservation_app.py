import unittest
from chambre import Chambre
from reservation import Reservation

class TestIntegrationReservationChambreComplexe(unittest.TestCase):
    def test_reservation_avec_promotion_et_saison(self):
        chambre = Chambre(102, 100)  # prix de base par nuit
        chambre.definir_prix_saison(1.5)  # Prix augmenté de 50% pour la saison haute
        reservation = Reservation(chambre, 3, 10)  # 3 nuits avec 10% de promotion
        
        self.assertEqual(reservation.calculer_cout(), 405)  # (100*1.5*3) * 0.9

    def test_annulation_avec_frais(self):
        chambre = Chambre(103, 100)
        reservation = Reservation(chambre, 5)  # 5 nuits sans promotion
        frais_annulation = reservation.annuler(50)  # Frais d'annulation fixés à 50
        
        self.assertTrue(reservation.est_annulee)
        self.assertEqual(frais_annulation, 50)

if __name__ == '__main__':
    unittest.main()
